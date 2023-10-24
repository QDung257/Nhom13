import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog, Scale
from PIL import Image, ImageTk

# Hàm xử lý sự kiện khi nút "Open Image" được nhấn
def open_image():
    global original_image
    file_path = filedialog.askopenfilename()
    if file_path:
        original_image = cv2.imread(file_path)
        show_image(original_image)

# Hàm xử lý sự kiện khi thanh trượt "Sharpness" thay đổi giá trị
def change_sharpness(val):
    global original_image
    if original_image is not None:
        sharpness = int(val)
        sharpened_image = enhance_sharpness(original_image, sharpness)
        show_image(sharpened_image)

# Hàm tạo ảnh với độ nét được tăng cường
def enhance_sharpness(image, sharpness):
    kernel = np.array([[-1, -1, -1],
                       [-1, sharpness + 8, -1],
                       [-1, -1, -1]])
    sharpened_image = cv2.filter2D(image, -1, kernel)
    return sharpened_image

# Hàm hiển thị ảnh trên giao diện
def show_image(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    img = ImageTk.PhotoImage(image=img)
    image_label.config(image=img)
    image_label.image = img

# Tạo cửa sổ Tkinter
root = tk.Tk()
root.title("OpenCV Image Filter with Adjustable Sharpness")
root.geometry('500x400')
# Tạo nút "Open Image"
open_button = tk.Button(root, text="Chọn ảnh", command=open_image)
open_button.pack()

# Tạo label để hiển thị ảnh
image_label = tk.Label(root)
image_label.pack()

# Biến lưu trữ ảnh gốc
original_image = None

# Tạo thanh trượt để điều chỉnh độ nét
sharpness_value = Scale(root, label="Sharpness", from_=0, to=5, orient="horizontal", command=change_sharpness)
sharpness_value.pack()

root.mainloop()
