import numpy as np
# 1
def task_10x10(n=10, m=10):
    A = np.zeros((n, m), dtype=np.int32)
    A[0, :-1] = 1
    A[0, -1] = 1
    return A

print(task_10x10())
print(task_10x10(5, 6))

# 2
def task_border(n=10, m=10):
    A = np.ones((n, m), dtype=np.int32)
    A[1:-1, 1:-1] = 0
    return A

print(task_border())
print(task_border(5, 4))

# 3
def task_2_5x5(n=5, m=5, num=2):
    A = np.full((n, m), num)
    return A

print(task_2_5x5())
print(task_2_5x5(4, 5, 9))

# 4
def task_0123(n=10, m=10):
    A = np.ones((n, m), dtype=np.int32)
    n, m = n // 2, m // 2
    A[:n, :m] = 0
    A[n:, :m] = 2
    A[n:, m:] = 3
    return A

print(task_0123())
print(task_0123(6, 6))
print(task_0123(8, 4))


# 5
def chess(n=10, m=10):
    A = np.zeros((n, m), dtype=np.int32)
    A[1::2, ::2] = 1
    A[::2, 1::2] = 1
    return A

print(chess())
print(chess(5, 3))


# 6
def task_1_to_9_lines(n=9, m=9):
    A = np.ones((n, m),dtype=np.int32)
    num = 2
    for i in range(1, n):
        A[i, :] = num
        num += 1
    return A

print(task_1_to_9_lines())
print(task_1_to_9_lines(3, 5))


# 7
def task_1_to_100(n=10, m=10):
    A = np.arange(1, n * m + 1).reshape(n, m)
    return A

print(task_1_to_100())
print(task_1_to_100(5, 6))


# 8
def task_multiplication_table(n=10, m=10):
    A = np.zeros((n, m), dtype=np.int32)
    num = 1
    for i in range(n):
        A[i, :] = range(num, (num * m + 1), num)
        num += 1
    return A

print(task_multiplication_table())
print(task_multiplication_table(7, 6))
print(task_multiplication_table(6, 7))


# 10
def task_double_chess(n=20, m=20):
    n, m = n // 2, m // 2
    A = np.tile(np.array([[0, 0, 1, 1], [0, 0, 1, 1], [1, 1, 0, 0], [1, 1, 0, 0]]), (n, m))
    return A

print(task_double_chess())
print(task_double_chess(2, 2))

