import numpy as np

n = np.random.randint(0, 10, size=[10, 10])
print(n)

num = int(input('შეიყვანეთ სვეტის ინდექსი: '))
res = np.delete(n, num, axis=1)
print(res)
