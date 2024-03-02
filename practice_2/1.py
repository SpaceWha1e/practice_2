import numpy as np

print('1 способ:\n', np.array([[1, 1], [1, 1]]), end='\n')
print('2 способ:\n',np.array([[1, 1] for i in range(2)]), end='\n')
print('3 способ:\n',np.array([[1 for i in range(2)]for j in range(2)]), end='\n')
print('4 способ:\n',np.ones((2, 2), dtype = int), end='\n')
print('5 способ:\n',np.full((2, 2), 1), end='\n')
