import numpy as np

n1 = np.random.randint(0, 10, size=[4, 4])
print(n1)
n2 = np.random.randint(0, 10, size=[4, 4])
print(n2)
print(np.multiply(n1, n2))

n3 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
n4 = np.array([[11, 12, 14, 15, 16], [11, 12, 14, 15, 16]])
print(np.multiply(n3, n4))
