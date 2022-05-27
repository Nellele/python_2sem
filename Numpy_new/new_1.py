import numpy as np

def divider(matrix, k):
    a = list(matrix)
    for i in range(len(a)-1):
        if a[i] % k == 0:
            del a[i]
    return np.array(a)


a = np.array([10, 20, 30, 40])
print(divider(a, 20))
