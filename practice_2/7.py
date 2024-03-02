import numpy as np


def three_min(A):
    mins = [[100 for i in range(3)], [0 for i in range(3)]]
    for i in range(0, len(A)):
        if A[i] < mins[0][2]:
            if A[i] >= mins[0][1]:
                mins[0][2] = A[i]
                mins[1][2] = i
            elif A[i] >= mins[0][0]:
                mins[0][2] = mins[0][1]
                mins[1][2] = mins[1][1]
                mins[0][1] = A[i]
                mins[1][1] = i
            elif A[i] < mins[0][0]:
                mins[0][2] = mins[0][1]
                mins[1][2] = mins[1][1]
                mins[0][1] = mins[0][0]
                mins[1][1] = mins[1][0]
                mins[0][0] = A[i]
                mins[1][0] = i
    return mins


A = np.random.randint(0, 100, 10)
print(three_min(A)[1])
