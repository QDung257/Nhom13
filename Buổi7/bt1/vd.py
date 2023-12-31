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

# Hàm xử lý sự kiện khi thanh trượt "Blur Radius" thay đổi giá trị
def change_blur_radius(val):
    global original_image
    if original_image is not None:
        blur_radius = int(blur_value.get())
        blurred_image = cv2.GaussianBlur(original_image, (blur_radius, blur_radius), 0)
        show_image(blurred_image)

# Hàm hiển thị ảnh trên giao diện
def show_image(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    img = ImageTk.PhotoImage(image=img)
    image_label.config(image=img)
    image_label.image = img

# Tạo cửa sổ Tkinter
root = tk.Tk()
root.title("OpenCV Image Filter with Adjustable Blur")
root.geometry('500x400')
# Tạo nút "Open Image"
open_button = tk.Button(root, text="Chọn ảnh", command=open_image)
open_button.pack()

# Tạo label để hiển thị ảnh
image_label = tk.Label(root)
image_label.pack()

# Biến lưu trữ ảnh gốc
original_image = None

# Tạo thanh trượt để điều chỉnh độ mờ
blur_value = Scale(root, label="Blur Radius", from_=1, to=10, orient="horizontal", command=change_blur_radius)
blur_value.pack()

root.mainloop()
