import numpy as np

def giai_he(A, B):
    try:
        A_inv = np.linalg.inv(A)  # Tạo ma trận nghịch đảo của ma trận hệ số A
        X = np.dot(A_inv, B)  # Tính nghiệm của hệ phương trình
        return X
    except np.linalg.LinAlgError:
        return "Hệ phương trình vô nghiệm hoặc vô số nghiệm."

# Ví dụ với hệ phương trình 3 phương trình và 3 ẩn:
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([10, 11, 12])

nghiem = giai_he(A, B)
print("Nghiệm của hệ phương trình là:", nghiem)

