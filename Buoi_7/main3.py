import cv2
import dlib
import numpy as np

# Đọc ảnh chân dung
img = cv2.imread('pic2.png')

# Tạo bộ phát hiện khuôn mặt
detector = dlib.get_frontal_face_detector()

# Phát hiện khuôn mặt trong ảnh
faces = detector(img)

# Tạo một mặt nạ trắng với cùng kích thước với ảnh
mask = np.zeros_like(img, dtype=np.uint8)

# Vẽ vùng trắng tương ứng với khuôn mặt lên mặt nạ
for face in faces:
    x, y, w, h = face.left(), face.top(), face.width(), face.height()
    cv2.rectangle(mask, (x, y), (x + w, y + h), (255, 255, 255), -1)

# Áp dụng bộ lọc Gaussian Blur chỉ cho vùng trắng trong mặt nạ
blurred_img = cv2.GaussianBlur(img, (0, 0), 5, dst=mask)

# Hiển thị ảnh
cv2.imshow('Blurred Image', blurred_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
