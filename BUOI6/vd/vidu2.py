import cv2

import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('pic1.jpg',cv2.IMREAD_GRAYSCALE)
a=float(input("Nhap a: "))
b=float(input("Nhap b: "))
half=cv2.resize(img,(0, 0), fx=a, fy=b)

x=int(input("Nhap khung1: "))
y=int(input("Nhap khung2: "))
bigger=cv2.resize(img,(x,y))

z=int(input("Nhap khung1: "))
t=int(input("Nhap khung2: "))
stretch_near = cv2.resize(img,(z,t), interpolation  = cv2.INTER_LINEAR)

Titles=["Original", "Half", "Bigger", "Interpolation Nearest"]
images=[img, half, bigger, stretch_near]
count=4
for i in range(count):
    plt.subplot(2, 2, i+1)
    plt.title(Titles[i])
    plt.imshow(images[i])

plt.show()
