import random
import time

time1 = time.time()

def juzheng(n):
    matrix = []
    for i in range(n):
        matrix.append([random.randint(1, 10) for _ in range(n)])
    return matrix

n = int(input("请输入矩阵的大小："))
A = juzheng(n)
B = juzheng(n)
C = [[0] * n for _ in range(n)]

# 行列转换，预先缓存 B 的列
B_T = list(zip(*B))

block_size = 64  # 块大小，可以根据具体情况调整

def block_multiply(A, B_T, C, n, block_size):
    for i0 in range(0, n, block_size):
        for j0 in range(0, n, block_size):
            for k0 in range(0, n, block_size):
                for i in range(i0, min(i0 + block_size, n)):
                    A_i = A[i]  # 缓存 A[i]
                    for j in range(j0, min(j0 + block_size, n)):
                        B_j = B_T[j]  # 缓存 B 的第 j 列
                        sum = 0
                        for k in range(k0, min(k0 + block_size, n)):
                            sum += A_i[k] * B_j[k]
                        C[i][j] += sum

start_time = time.time()
block_multiply(A, B_T, C, n, block_size)
end_time = time.time()
elapsed_time = end_time - start_time

print(f"矩阵乘法耗时{elapsed_time:.6f}秒")