import random
import time
import psutil
import numpy as np
process = psutil.Process()
def juzheng(n): # 生成一个n*n的矩阵
    martix = []
    for i in range(n):
        martix.append([random.randint(1,10) for i in range(n)])
    return martix
time1 = time.time()
n = int(input("请输入矩阵的大小："))
A = juzheng(n)
B = juzheng(n)
C = [[0 for i in range(n)] for i in range(n)]
C=np.dot(A,B)
cpu1 = process.cpu_percent(interval=1)
time2 = time.time()
print(f"CPU使用率{cpu1:.2f}%")
time3 = time2 - time1
print(f"矩阵乘法耗时{time3:.6f}秒")

