import sys
import cv2
import face_recognition
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QMainWindow
from PyQt5.QtCore import QTimer, QDateTime, Qt
from PyQt5.QtGui import QPixmap, QImage, QFont
from datetime import datetime, timedelta

# Ảnh đầu vào để nhận diện
user_image = face_recognition.load_image_file("person2.jpg") #Ảnh 
user_face_encoding = face_recognition.face_encodings(user_image)[0]

class FaceUnlockApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Mở khóa màn hình"
        self.code = "1234"
        self.entered_code = ""
        self.face_unlock_enabled = False
        self.recognized_person = "Không xác định"
        self.failed_attempts = 0
        self.lockout_time = None
        self.face_unlock_delay = 5  # Đợi 5 giây trước khi quay lại giao diện mặc định
        self.face_unlock_timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()

        # Sử dụng CSS để thay đổi màu sắc cho các thành phần giao diện
        self.message_label = QLabel("Nhập mã hoặc dùng mở khóa bằng khuôn mặt", self)
        self.message_label.setStyleSheet("color: blue; font-size: 16px;")
        layout.addWidget(self.message_label)

        self.code_input = QLineEdit(self)
        self.code_input.setPlaceholderText("Nhập mật khẩu")
        self.code_input.setStyleSheet("background-color: white; font-size: 16px;")
        layout.addWidget(self.code_input)

        code_button = QPushButton("Nhập mật khẩu", self)
        code_button.setStyleSheet("background-color: white; color: black; font-size: 16px;")
        code_button.clicked.connect(self.unlock_with_code)
        layout.addWidget(code_button)

        face_unlock_button = QPushButton("Chuyển đổi mở khóa khuôn mặt", self)
        face_unlock_button.setStyleSheet("background-color: white; color: black; font-size: 16px;")
        face_unlock_button.clicked.connect(self.toggle_face_unlock)
        layout.addWidget(face_unlock_button)

        self.image_label = QLabel(self)
        layout.addWidget(self.image_label)

        self.info_label = QLabel(self)
        self.info_label.setStyleSheet("color: red; font-size: 16px;")
        layout.addWidget(self.info_label)

        self.central_widget.setLayout(layout)

        self.cap = cv2.VideoCapture(0)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_camera_image)
        self.timer.start(100)# quét liên tục cho đến khi nhận diện được (100ms)

        self.face_unlock_timer.timeout.connect(self.return_to_default_interface)

    def unlock_with_code(self):
        if self.face_unlock_enabled:
            self.message_label.setText("Mở khóa khuôn mặt đang được bật. Vui lòng dùng khuôn mặt để mở khóa.")
        else:
            if self.lockout_time is not None and datetime.now() < self.lockout_time:
                remaining_time = self.lockout_time - datetime.now()
                self.message_label.setText(f"Thử lại sau {remaining_time.seconds} giây.")
            else:
                if self.code_input.text() == self.code:
                    self.message_label.setText("Mở khóa thành công!")
                    self.entered_code = ""
                    self.failed_attempts = 0
                else:
                    self.failed_attempts += 1
                    if self.failed_attempts >= 5:
                        self.lockout_time = datetime.now() + timedelta(minutes=1)  # Khóa trong 1 phút
                    self.message_label.setText("Mở khóa thất bại! Vui lòng thử lại.")
                self.code_input.clear()

    def toggle_face_unlock(self):
        if self.face_unlock_timer.isActive():
            self.face_unlock_timer.stop()
        if self.face_unlock_enabled:
            self.message_label.setText("Nhập mã hoặc mở bằng khuôn mặt")
        else:
            self.message_label.setText("Mở khóa bằng khuôn mặt đang được bật.")
            
            self.face_unlock_timer.start(self.face_unlock_delay * 1000)

        self.face_unlock_enabled = not self.face_unlock_enabled

    def update_camera_image(self):
        if self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                if self.face_unlock_enabled:
                    face_locations = face_recognition.face_locations(frame)
                    face_encodings = face_recognition.face_encodings(frame, face_locations)
                    self.recognized_person = "Không xác định được"
                    for face_encoding in face_encodings:
                        matches = face_recognition.compare_faces([user_face_encoding], face_encoding)
                        if True in matches:
                            self.recognized_person = "User: Quang Dũng"
                            self.message_label.setText("Mở khóa thành công!")
                            if self.face_unlock_timer.isActive():
                                self.face_unlock_timer.stop()
                            break

                height, width, channel = frame.shape
                bytesPerLine = 3 * width
                qImg = QImage(frame.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()

                pixmap = QPixmap.fromImage(qImg)
                self.image_label.setPixmap(pixmap)

                # Cập nhật thông tin người được công nhận
                self.info_label.setText(self.recognized_person)

    def return_to_default_interface(self):
        self.face_unlock_enabled = False
        self.message_label.setText("Nhập mã hoặc dùng mở bằng khuôn mặt")
        self.face_unlock_timer.stop()

    def closeEvent(self, event):
        self.cap.release()
        super(FaceUnlockApp, self).closeEvent(event)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    unlock_app = FaceUnlockApp()
    unlock_app.setWindowTitle(unlock_app.title)
    unlock_app.show()
    sys.exit(app.exec_())
