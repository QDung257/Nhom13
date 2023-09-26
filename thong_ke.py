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
i, = np.where(diemD == maxd)
mind = diemD.min()
i, = np.where(diemA == mind)

 
print('lop co nhieu diem D la {0} co {1} sv dat diem D'.format(in_data[i,0],maxd))
print('lop co it diem D la {0} co {1} sv dat diem D'.format(in_data[i,0],mind))
plt.plot(range(len(diemA)),diemA,'r-',label="Diem A")
plt.plot(range(len(diemB)),diemB,'g-',label="Diem B")
plt.plot(range(len(diemC)),diemC,'b-',label="Diem C")
plt.plot(range(len(diemD)),diemD,'y-',label="Diem D")
plt.xlabel('Lơp')
plt.ylabel(' So sv dat diem ')
plt.legend(loc='upper right')
plt.show()
      
