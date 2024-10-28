import numpy as np
from sklearn.model_selection import train_test_split

x = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14],
              [15, 16],[17, 18], [19,20], [21, 22], [23, 24]])
y = np.array([0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0])

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=3, random_state=42,suffle=False)

print("X_train:")
print(x_train)
print("X_test:")
print(x_test)
print("Y_train:")
print(y_train)
print("Y_test:")
print(y_test)
