import numpy as np


def nonzero(A):
    for i in range(100):
        for j in range(100):
            if A[i][j] == 1:
                return i + 1, j + 1


A = np.zeros((100, 100))
rng = np.random.default_rng()
A[int(rng.random() * 100), int(rng.random() * 100)] = 1
print(nonzero(A))
print(A)
