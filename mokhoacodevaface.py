import sys
import cv2
import face_recognition
import threading
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QMainWindow
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QPixmap, QImage, QPainter

# Load the user's face encoding
user_image = face_recognition.load_image_file("person2.jpg")
user_face_encoding = face_recognition.face_encodings(user_image)[0]

class FaceUnlockApp(QMainWindow):
    def __init__(self):
        super(FaceUnlockApp, self).__init__()
        self.title = "Face Unlock App"
        self.code = "1234"
        self.entered_code = ""
        self.face_unlock_enabled = False
        self.initUI()

    def initUI(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()

        self.message_label = QLabel("Enter Code or Enable Face Unlock")
        layout.addWidget(self.message_label)

        self.code_input = QLineEdit()
        self.code_input.setPlaceholderText("Enter Code")
        layout.addWidget(self.code_input)

        code_button = QPushButton("Unlock with Code")
        code_button.clicked.connect(self.unlock_with_code)
        layout.addWidget(code_button)

        face_unlock_button = QPushButton("Toggle Face Unlock")
        face_unlock_button.clicked.connect(self.toggle_face_unlock)
        layout.addWidget(face_unlock_button)

        self.image_label = QLabel(self)
        layout.addWidget(self.image_label)

        self.central_widget.setLayout(layout)

        # Initialize the camera capture
        self.cap = cv2.VideoCapture(0)

        # Create a timer to continuously update the camera image
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_camera_image)
        self.timer.start(100)  # Update every 100 milliseconds

    def unlock_with_code(self):
        if self.face_unlock_enabled:
            self.message_label.setText("Face Unlock is enabled. Please use Face Unlock.")
        else:
            if self.code_input.text() == self.code:
                self.message_label.setText("Unlock Successful!")
                self.entered_code = ""
            else:
                self.message_label.setText("Unlock Failed. Please try again.")
            self.code_input.clear()

    def toggle_face_unlock(self):
        self.face_unlock_enabled = not self.face_unlock_enabled
        if self.face_unlock_enabled:
            self.message_label.setText("Face Unlock is enabled.")
        else:
            self.message_label.setText("Enter Code or Enable Face Unlock")

    def update_camera_image(self):
        if self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                if self.face_unlock_enabled:
                    face_locations = face_recognition.face_locations(frame)
                    face_encodings = face_recognition.face_encodings(frame, face_locations)
                    for face_encoding in face_encodings:
                        matches = face_recognition.compare_faces([user_face_encoding], face_encoding)
                        if True in matches:
                            self.message_label.setText("Mở khóa thành công!")
                        else:
                            self.message_label.setText("Không nhận diện được!")
                            break

                height, width, channel = frame.shape
                bytesPerLine = 3 * width
                qImg = QImage(frame.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()

                pixmap = QPixmap.fromImage(qImg)
                self.image_label.setPixmap(pixmap)

    def closeEvent(self, event):
        self.cap.release()
        super(FaceUnlockApp, self).closeEvent(event)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    unlock_app = FaceUnlockApp()
    unlock_app.setWindowTitle(unlock_app.title)
    unlock_app.show()
    sys.exit(app.exec_())
