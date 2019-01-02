import numpy as np

array = np.array([[[1, 2, 3], [1, 2, 3]], [[1, 2, 3], [1, 2, 3]]])

array_trans = np.sum(array, axis=2)

a = np.array([1,2,3])

b = a.reshape(-1,1)

c = b.reshape(1,3)

print("debug")
