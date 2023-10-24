import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

# Hàm xử lý sự kiện khi nút "Chọn ảnh" được nhấn
def open_image():
    global image
    file_path = filedialog.askopenfilename()
    if file_path:
        image = cv2.imread(file_path)
        show_image(image)

# Hàm xử lý sự kiện khi nút "Làm mịn" được nhấn
def apply_blur():
    global image
    if image is not None:
        blurred_image = cv2.GaussianBlur(image, (0, 0), 5)
        show_image(blurred_image)

# Hàm xử lý sự kiện khi nút "Làm nét" được nhấn
def apply_sharpen():
    global image
    global img
    if image is not None:
        kernel = np.array([[-1, -1, -1],
                           [-1, 9, -1],
                           [-1, -1, -1]])
        sharpened_image = cv2.filter2D(image, -1, kernel)
        show_image(sharpened_image)

# Hàm hiển thị ảnh trên giao diện
def show_image(img):
    global image
    global s_image
    
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    img = ImageTk.PhotoImage(image=img)
    image_label.config(image=img)
    image_label.image = img

# Tạo cửa sổ Tkinter
root = tk.Tk()
root.title("OpenCV Image Filters")
root.geometry('500x400')
# Tạo nút "Chọn ảnh"
open_button = tk.Button(root, text="Chọn ảnh", command=open_image)
open_button.pack()

# Tạo nút "làm mịn"
blur_button = tk.Button(root, text="Làm mịn", command=apply_blur)
blur_button.pack()

# Tạo nút "làm nét"
sharpen_button = tk.Button(root, text="Làm nét", command=apply_sharpen)
sharpen_button.pack()

# Tạo label để hiển thị ảnh
image_label = tk.Label(root)
image_label.pack()


# Biến lưu trữ ảnh
image = None

root.mainloop()
