import numpy as np
import tensorflow.compat.v1 as tf
import pandas as pd
import matplotlib.pyplot as plt

tf.disable_v2_behavior()

# Đọc dữ liệu từ tệp CSV
df = pd.read_csv('Student_Performance.csv')

# Lấy các cột dữ liệu từ tệp CSV
x1 = df['Hours Studied'].values
x2 = df['Previous Scores'].values
x3 = df['Extracurricular Activities'].values
x4 = df['Sleep Hours'].values
x5 = df['Sample Question Papers Practiced'].values

# Tạo giá trị ngẫu nhiên cho y trong khoảng từ 1 đến 50
y = np.random.randint(1, 51, len(x1))

n = len(x1)  # Số lượng dữ liệu

# Tạo placeholders cho dữ liệu đầu vào và đầu ra
X1 = tf.placeholder("float")
X2 = tf.placeholder("float")
X3 = tf.placeholder("float")
X4 = tf.placeholder("float")
X5 = tf.placeholder("float")
Y = tf.placeholder("float")

# Khởi tạo các biến trọng số và sai số
W1 = tf.Variable(np.random.randn(), name="W1")
W2 = tf.Variable(np.random.randn(), name="W2")
W3 = tf.Variable(np.random.randn(), name="W3")
W4 = tf.Variable(np.random.randn(), name="W4")
W5 = tf.Variable(np.random.randn(), name="W5")
b = tf.Variable(np.random.randn(), name="b")

# Thiết lập tốc độ học
learning_rate = 0.01

# Số vòng lặp huấn luyện
training_epochs = 100

# Hàm dự đoán theo công thức mới
y_pred = W1 * X1 + W2 * X2 + W3 * X3 + W4 * X4 + W5 * X5 + b

# Hàm mất mát
cost = tf.reduce_sum(tf.pow(y_pred - Y, 2)) / (2 * n)

# Tối ưu hóa bằng Gradient Descent
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

# Khởi tạo biến
init = tf.global_variables_initializer()

# Bắt đầu phiên tính toán TensorFlow
with tf.Session() as sess:
    sess.run(init)

    for epoch in range(training_epochs):
        for (_x1, _x2, _x3, _x4, _x5, _y) in zip(x1, x2, x3, x4, x5, y):
            sess.run(optimizer, feed_dict={X1: _x1, X2: _x2, X3: _x3, X4: _x4, X5: _x5, Y: _y})

        if (epoch + 1) % 50 == 0:
            c = sess.run(cost, feed_dict={X1: x1, X2: x2, X3: x3, X4: x4, X5: x5, Y: y})
            print("Epoch", (epoch + 1), ": cost =", c, "W1 =", sess.run(W1), "W2 =", sess.run(W2), "W3 =", sess.run(W3), "W4 =", sess.run(W4), "W5 =", sess.run(W5), "b =", sess.run(b))

    training_cost = sess.run(cost, feed_dict={X1: x1, X2: x2, X3: x3, X4: x4, X5: x5, Y: y})
    weight1 = sess.run(W1)
    weight2 = sess.run(W2)
    weight3 = sess.run(W3)
    weight4 = sess.run(W4)
    weight5 = sess.run(W5)
    bias = sess.run(b)

# Calculate the predictions
predictions = weight1 * x1 + weight2 * x2 + weight3 * x3 + weight4 * x4 + weight5 * x5 + bias
print("Training cost =", training_cost, "Weight 1 =", weight1, "Weight 2 =", weight2, "Weight 3 =", weight3, "Weight 4 =", weight4, "Weight 5 =", weight5, "bias =", bias, '\n')

# Plotting the Results
plt.plot(x1, y, 'ro', label='Original data')
plt.plot(x1, predictions, label='Fitted line')
plt.title('Linear Regression Result')
plt.legend()
plt.show()
