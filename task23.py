import numpy as np

n = np.random.randint(0, 10, size=[10, 10])
n1 = np.random.randint(0, 10, size=[10, 10])

print(np.concatenate((n, n1), axis=0).flatten())
