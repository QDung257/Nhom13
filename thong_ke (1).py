import pandas as pd
from numpy import array
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_csv('diemPython.csv',index_col=0,header = 0)
in_data = array(df.iloc[:,:])
print(in_data)
print('Tong so sinh vien tham du mon hoc la :')
tongsv= in_data[:,1]
print(np.sum(tongsv))
diemA = in_data[:,3]
diemB = in_data[:,5]
diemC = in_data[:,7]
diemD = in_data[:,9]
diemF = in_data[:,10]
print('Tong sv:',tongsv)
tongdiema = np.sum(diemA)
print("Tong so sinh vien dat diem A la: ",tongdiema)
tongdiemb = np.sum(diemB)
print("Tong so sinh vien dat diem B la: ",tongdiemb)
tongdiemc = np.sum(diemC)
print("Tong so sinh vien dat diem C la: ",tongdiemc)
tongdiemd = np.sum(diemD)
print("Tong so sinh vien dat diem D la: ",tongdiemd)
tongdiemf = np.sum(diemF)
print("Tong so sinh vien dat diem F la: ",tongdiemf)
maxd = diemD.max()
maxd_class_indices = np.where(diemD == maxd)[0]  # Using [0] to get the class indices as an array
mind = diemD.min()
mind_class_indices = np.where(diemD == mind)[0]  # Using [0] to get the class indices as an array

print('Lop co nhieu diem D cao nhat la:')
for i in maxd_class_indices:
    print(f'{in_data[i, 0]} co diem D cao nhat la {maxd}')

print('Lop co it diem D thap nhat la:')
for i in mind_class_indices:
    print(f'{in_data[i, 0]} co diem D thap nhat la {mind}')

plt.plot(range(len(diemA)),diemA,'r-',label="Diem A")
plt.plot(range(len(diemB)),diemB,'g-',label="Diem B")
plt.plot(range(len(diemC)),diemC,'b-',label="Diem C")
plt.plot(range(len(diemD)),diemD,'y-',label="Diem D")
plt.xlabel('Lơp')
plt.ylabel(' So sv dat diem ')
plt.legend(loc='upper right')
plt.show()
      
