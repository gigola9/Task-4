import numpy as np

n = np.random.randint(0, 10, size=[10, 10])
print(n)

res = np.where(n == 0, 1, n)
print(res)
