import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

# Hàm để cập nhật và hiển thị ảnh sau khi zoom và quay ảnh
def update_image():
    rotated_img = cv2.warpAffine(original_img, cv2.getRotationMatrix2D((original_img.shape[1] / 2, original_img.shape[0] / 2), current_rotation, 1), (original_img.shape[1], original_img.shape[0]))
    scaled_img = cv2.resize(rotated_img, None, fx=current_scale, fy=current_scale, interpolation=cv2.INTER_LINEAR)
    img = cv2.cvtColor(scaled_img, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    img = ImageTk.PhotoImage(img)
    img_label.config(image=img)
    img_label.image = img
def select_image():
    global original_img, current_scale, current_rotation
    filename = filedialog.askopenfilename()
    if filename:
        original_img = cv2.imread(filename)
        current_scale = 1.0
        current_rotation = 0
        update_image()
def change_scale():
    global current_scale
    scale_text = scale_entry.get()
    try:
        scale_value = float(scale_text)
        if current_choice.get() == 1:
            current_scale = scale_value
        elif current_choice.get() == 2:
            current_scale = 1 / scale_value
        update_image()
    except ValueError:
        pass
# Tạo cửa sổ
window = tk.Tk()
window.title("Tỉ lệ ảnh")
# Khai báo biến toàn cục
current_scale = 1.0
current_rotation = 0
original_img = None
scale_factor = 1.2
current_choice = tk.IntVar()
current_choice.set(1)
# Tạo nút "Chọn ảnh" 
select_button = tk.Button(window, text="Chọn ảnh", command=select_image)
select_button.pack()

# Tạo hộp văn bản để nhập tỷ lệ zoom
scale_label = tk.Label(window, text="Nhập tỷ lệ zoom:")
scale_label.pack()
scale_entry = tk.Entry(window)
scale_entry.pack()
scale_confirm_button = tk.Button(window, text="Xác nhận", command=change_scale)
scale_confirm_button.pack()
# Tạo label để hiển thị ảnh
img_label = tk.Label(window)
img_label.pack()

window.mainloop()
