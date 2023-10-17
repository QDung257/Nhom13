import numpy as np

def nhap_matran(n):
    """
    Hàm nhập ma trận hệ số từ người dùng.
    n: Số chiều của ma trận (số phương trình và số ẩn).
    Trả về ma trận hệ số A và vector vế phải B.
    """
    print("Nhập ma trận hệ số A:")
    A = []
    for i in range(n):
        row = list(map(float, input().split()))
        A.append(row)

    print("Nhập vector vế phải B:")
    B = list(map(float, input().split()))

    return np.array(A), np.array(B)

def giai_he_phuong_trinh(A, B):
    """
    Hàm giải hệ phương trình tuyến tính.
    A: Ma trận hệ số.
    B: Vector vế phải.
    Trả về một vector chứa nghiệm của hệ phương trình hoặc None nếu không có nghiệm.
    """
    try:
        n = len(A)
        X = np.linalg.solve(A, B)
        return X
    except np.linalg.LinAlgError:
        return None

def in_nghiem(X):
    """
    Hàm in ra nghiệm của hệ phương trình.
    X: Vector chứa nghiệm.
    """
    if X is not None:
        print("Nghiệm của hệ phương trình:")
        for i in range(len(X)):
            print(f"x{i+1} =", X[i])
    else:
        print("Hệ phương trình vô nghiệm.")

# Ví dụ sử dụng
n = int(input("Nhập số phương trình và số ẩn trong hệ: "))
A, B = nhap_matran(n)
X = giai_he_phuong_trinh(A, B)
in_nghiem(X)
