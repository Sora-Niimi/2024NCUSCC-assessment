import numpy as np
import multiprocessing
import time
import psutil
import os

# 矩阵乘法函数
def 矩阵乘法(A, B):
    return np.dot(A, B)

# 获取所有子进程的内存使用情况
def get_memory_usage(process):
    memory_usage = process.memory_info().rss  # 获取主进程的内存使用情况
    for child in process.children(recursive=True):
        memory_usage += child.memory_info().rss  # 累加所有子进程的内存使用情况
    return memory_usage / 1024 / 1024  # 转换为 MB

# 验证计算结果是否正确
def 验证结果(C, reference_C):
    return np.allclose(C, reference_C)

# 将矩阵分块
def 分块矩阵(A, B, num_blocks):
    n = A.shape[0]
    block_size = n // num_blocks
    A_blocks = [A[i*block_size:(i+1)*block_size, :] for i in range(num_blocks)]
    B_blocks = [B[i*block_size:(i+1)*block_size, :] for i in range(num_blocks)]
    return A_blocks, B_blocks

# 主函数
def 主函数(matrix_size, num_experiments, num_processes):
    # 生成随机矩阵
    A = np.random.rand(matrix_size, matrix_size)
    B = np.random.rand(matrix_size, matrix_size)
    
    # 计算参考结果
    reference_C = np.dot(A, B)
    
    # 记录每次实验的耗时和内存使用情况
    耗时 = []
    内存使用 = []
    
    for _ in range(num_experiments):
        开始时间 = time.time()
        
        try:
            # 使用 multiprocessing 并行计算矩阵乘法
            process = psutil.Process(os.getpid())
            
            # 将矩阵分块
            A_blocks, B_blocks = 分块矩阵(A, B, num_processes)
            
            # 并行计算每个块的乘积
            with multiprocessing.Pool(processes=num_processes) as pool:
                C_blocks = pool.starmap(矩阵乘法, [(A_blocks[i], B) for i in range(num_processes)])
            
            # 合并结果
            C = np.vstack(C_blocks)
            
            结束时间 = time.time()
            耗时.append(结束时间 - 开始时间)
            
            # 获取内存使用情况
            memory_usage = get_memory_usage(process)
        except Exception as e:
            print(f"计算过程中出现错误: {e}")
            C = None
            memory_usage = 0
            continue
        
        # 记录内存使用情况
        内存使用.append(memory_usage)
    
    # 打印每次实验的耗时和内存使用情况
    for i, (t, mem) in enumerate(zip(耗时, 内存使用)):
        print(f"实验 {i + 1}: {t:.6f} 秒, 内存使用: {mem:.2f} MB")
    
    # 验证计算结果是否正确
    if C is not None and 验证结果(C, reference_C):
        print("计算结果正确。")
    else:
        print("计算结果错误。")

if __name__ == "__main__":
    # 输入矩阵规模、实验次数和进程数
    矩阵规模 = int(input("请输入矩阵规模: "))
    实验次数 = int(input("请输入实验次数: "))
    进程数 = int(input("请输入进程数: "))
    
    主函数(矩阵规模, 实验次数, 进程数)