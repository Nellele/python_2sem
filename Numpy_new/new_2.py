import numpy as np

def even_num(matrix):
    a = list(matrix)
    for i in range(len(a)):
        if a[i] % 2 == 0:
            a[i] /= 2
    return np.array(a)

a = np.array([10, 20, 30, 40])
print(even_num(a))
