import sympy as sym
x=sym.Symbol('x')
y=sym.Symbol('y')
z=sym.Symbol('z')
fx=input("Nhap bieu thuc: ")
a=int(input("Đạo hàm bậc: "))
daohamx=sym.diff(fx,x,a)
daohamy=sym.diff(fx,y,a)
daohamz=sym.diff(fx,z,a)
print("Đạo hàm theo biến x của hàm số trên là: ",daohamx)
print("Đạo hàm theo biến y của hàm số trên là: ",daohamy)
print("Đạo hàm theo biến y của hàm số trên là: ",daohamz)

#tính tích phân và giá trị tích phân
f=input("Nhap bieu thuc can tinh tich phan: ")
tp=[]
tichphan = sym.integrate(f,x)
print("Tích phân của hàm số trên là: ",tichphan)
b=float(input("Nhap gia tri dau: "))
c=float(input("Nhap gia tri cuoi: "))
kqtichphan = sym.integrate(f,(x,b,c))
print("Giá trị của hàm số trong đoạn trên là: ",kqtichphan)
#khai triển biểu thức:
print("Khai triển biểu thức: ",sym.expand((fx)))
print("Rút gọn biểu thức: ",sym.simplify((f)))
      
