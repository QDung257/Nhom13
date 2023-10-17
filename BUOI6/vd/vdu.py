from tkinter import *
from tkinter.filedialog import askopenfilename
import cv2
import tkinter.messagebox
import pathlib
from PIL import Image
import numpy as np
win = Tk()
win.title("chinhsuaanh")
win.geometry('500x100')

# Tạo nhãn để hiển thị ảnh gốc

image = None
img = None
def select_image():
    global image
    global tk_image
    global xoay
    global zoom
    # Mở hộp thoại chọn ảnh
    filename = askopenfilename(filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png"), ("GIF", "*.gif"), ("BMP", "*.bmp")])
    cv2.destroyAllWindows()
    xoay = 0
    zoom = 1
    # Nếu người dùng chọn ảnh
    if filename:
        # Đọc ảnh và lưu vào biến image
        image = cv2.imread(filename)
        img = image.copy()
        cv2.imshow("Anh Goc", img)
    else:
        # Nếu người dùng không chọn ảnh, hiển thị thông báo
        tkinter.messagebox.showwarning("Cảnh báo", "Bạn chưa chọn ảnh!")

def nut1():
    global image
    global s_image
    global img
    # Kiểm tra xem ảnh đã được chọn chưa
    if (image is None):
        tkinter.messagebox.showwarning("Cảnh báo", "Bạn chưa chọn ảnh!")
        return
    img = cv2.flip(image, 1)
    cv2.imshow('Lat', img)

def nut2():
    global image
    global s_image
    global zoom
    global img

    # Kiểm tra xem ảnh đã được chọn chưa
    if (image is None):
        tkinter.messagebox.showwarning("Cảnh báo", "Bạn chưa chọn ảnh!")
        return
    if (zoom>=1.3): zoom=1.3
    zoom = zoom + 0.1
    img = cv2.resize(image, dsize=(int(image.shape[1] * zoom), int(image.shape[0] * zoom)), interpolation=cv2.INTER_CUBIC)
    cv2.imshow('zoom', img)
def nut3():
    global image
    global s_image
    global zoom
    global img
    # Kiểm tra xem ảnh đã được chọn chưa
    if (image is None):
        tkinter.messagebox.showwarning("Cảnh báo", "Bạn chưa chọn ảnh!")
        return
    if (zoom <= 0.7): zoom = 0.7
    zoom = zoom - 0.1
    img = cv2.resize(image, dsize=(int(image.shape[1] * zoom), int(image.shape[0] * zoom)), interpolation=cv2.INTER_CUBIC)
    cv2.imshow('zoom', img)

def nut4():

    global image
    global s_image
    global dem
    global img
    # Kiểm tra xem ảnh đã được chọn chưa
    if (image is None):
        tkinter.messagebox.showwarning("Cảnh báo", "Bạn chưa chọn ảnh!")
        return
    dem = dem + 1
    if (dem % 4 == 0):
        cv2.imshow('Xoay', image)
    elif (dem % 4 == 1):
        img = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
        cv2.imshow('Xoay', img)
    elif (dem % 4 == 2):
        img = cv2.rotate(image, cv2.ROTATE_180)
        cv2.imshow('Xoay', img)
    elif (dem % 4 == 3):
        img = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
        cv2.imshow('Xoay', img)


    
bt1 = Button(win, text="zoom in", command=nut2)
bt1.place(x=120, y=10)
bt2 = Button(win, text="Zoom out", command=nut3)
bt2.place(x=190, y=10)
bt3 = Button(win, text="Xoay", command=nut4)
bt3.place(x=260, y=10)


button = Button(win, text="Chọn ảnh", command=lambda: select_image())
button.place(x=50, y=10)

win.mainloop()
