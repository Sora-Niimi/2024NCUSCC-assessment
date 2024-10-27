from mpi4py import MPI
import time
import numpy as np
import psutil

def get_memory_usage():
    process = psutil.Process()
    memory_usage = process.memory_info().rss  # 获取主进程的内存使用情况
    for child in process.children(recursive=True):
        memory_usage += child.memory_info().rss  # 累加所有子进程的内存使用情况
    return memory_usage / 1024 / 1024  # 转换为 MB

def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    if rank == 0:
        # 输入矩阵大小和执行次数
        N = int(input("请输入矩阵大小："))
        num_executions = int(input("请输入执行次数："))
    else:
        N = None
        num_executions = None

    # 广播矩阵大小和执行次数给所有进程
    N = comm.bcast(N, root=0)
    num_executions = comm.bcast(num_executions, root=0)

    if rank == 0:
        # 生成大矩阵 A 和 B
        A = np.random.rand(N, N)
        B = np.random.rand(N, N)
        
        # 将矩阵 A 分块
        chunks = np.array_split(A, size, axis=0)
    else:
        A = None
        B = None
        chunks = None

    # 将 A 的块分发给所有进程
    local_A = comm.scatter(chunks, root=0)

    # 广播矩阵 B 给所有进程
    B = comm.bcast(B, root=0)

    # 记录每次实验的耗时和内存使用情况
    耗时 = []
    内存使用 = []

    for _ in range(num_executions):
        comm.Barrier()  # 同步所有进程
        开始时间 = time.time()
        
        # 进行矩阵乘法
        local_C = np.dot(local_A, B)
        
        comm.Barrier()  # 同步所有进程
        结束时间 = time.time()
        耗时.append(结束时间 - 开始时间)
        
        # 获取内存使用情况
        memory_usage = get_memory_usage()
        内存使用.append(memory_usage)

    #收集所有进程的计算结果
    C = comm.gather(local_C, root=0)

    if rank == 0:
        # 合并结果
        C = np.vstack(C)
        
        # 打印每次实验的耗时和内存使用情况
        for i, (t, mem) in enumerate(zip(耗时, 内存使用)):
            print(f"实验 {i + 1}: {t:.6f} 秒, 内存使用: {mem:.2f} MB")
        
        # 验证计算结果是否正确
        reference_C = np.dot(A, B)
        if np.allclose(C, reference_C):
            print("计算结果正确。")
        else:
            print("计算结果错误。")

if __name__ == "__main__":
    main()