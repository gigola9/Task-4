import numpy as np

n = np.random.randint(0, 10, size=[10, 10])
flt = n.flatten()
print(n)

num = int(input('შეიყვანეთ რიცხვი: '))

print(np.delete(flt, np.argwhere(flt == num)))
