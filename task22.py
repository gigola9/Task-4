import numpy as np

chess = np.zeros((8, 8), dtype=int)
chess[1::2, ::2] = 1
chess[::2, 1::2] = 1
print(chess)
