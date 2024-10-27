import psutil
import time
import numpy as np

# 获取当前进程
process = psutil.Process()

# 获取内存使用情况
memory_info = process.memory_info()
memory_usage_mb = memory_info.rss / 1024 / 1024  # 转换为 MB
print(f"内存使用: {memory_usage_mb:.2f} MB")

# 获取 CPU 使用率
cpu_usage = process.cpu_percent(interval=1)  # 1秒间隔
print(f"CPU 使用率: {cpu_usage:.2f}%")

# 持续监控内存和 CPU 使用情况
print("持续监控内存和 CPU 使用情况（按 Ctrl+C 退出）")
try:
    while True:
        # 执行一些更复杂的任务（矩阵乘法）
        A = np.random.rand(1000, 1000)
        B = np.random.rand(1000, 1000)
        C = np.dot(A, B)
        
        memory_info = process.memory_info()
        memory_usage_mb = memory_info.rss / 1024 / 1024  # 转换为 MB
        cpu_usage = process.cpu_percent(interval=1)  # 1秒间隔
        print(f"内存使用: {memory_usage_mb:.2f} MB, CPU 使用率: {cpu_usage:.2f}%")
        time.sleep(1)
except KeyboardInterrupt:
    print("监控结束")