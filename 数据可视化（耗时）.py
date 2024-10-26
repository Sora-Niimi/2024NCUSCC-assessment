import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 设置中文字体
font = FontProperties(fname='C:/Windows/Fonts/simsun.ttc')  # 你可以根据你的系统字体路径进行调整

# 创建数据字典
data_dict = {
    '优化情况': ['mpi4y'] * 7 + ['joblib'] * 7 + ['multiprocessing'] * 3,
    '项目规模': [10000, 10000, 10000, 8000, 4000, 2000, 1000, 1000, 2000, 4000, 8000, 10000, 10000, 10000, 10000, 10000, 10000],
    '进程数': [4, 2, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2, 1, 4, 2, 1],
    '平均耗时（秒）': [40.14404033, 45.58187767, 59.73926433, 15.12474867, 1.957008333, 0.281834, 0.082977, 0.378722667, 0.75945, 3.005522, 18.81784333, 38.36970167, 35.084648, 30.834548, 103.6220017, 69.22675867, 54.760433],
    '平均使用（MB）': [1889.383333, 2347.956667, 3120.396667, 1277.16, 379.6, 134.8133333, 71.87, 319.12, 479.9733333, 1058.383333, 2764.333333, 3898.37, 3834.633333, 3879.833333, 3459.333333, 3523.533333, 3708.586667]
}

# 将数据字典转换为 DataFrame
df = pd.DataFrame(data_dict)

# 过滤数据
df_mpi4py_4 = df[(df['优化情况'] == 'mpi4y') & (df['进程数'] == 4)]
df_mpi4py_10000 = df[(df['优化情况'] == 'mpi4y') & (df['项目规模'] == 10000)]
df_joblib_4 = df[(df['优化情况'] == 'joblib') & (df['进程数'] == 4)]
df_joblib_10000 = df[(df['优化情况'] == 'joblib') & (df['项目规模'] == 10000)]
df_multiprocessing_10000 = df[(df['优化情况'] == 'multiprocessing') & (df['项目规模'] == 10000)]
df_all_10000_4 = df[(df['项目规模'] == 10000) & (df['进程数'] == 4)]

# 绘制使用 mpi4y 且进程数都为 4 的条形图
plt.figure(figsize=(12, 6))
plt.bar(df_mpi4py_4['项目规模'].astype(str), df_mpi4py_4['平均耗时（秒）'], label='mpi4y')
plt.title('使用 mpi4y 且进程数都为 4 的平均耗时', fontproperties=font)
plt.xlabel('项目规模', fontproperties=font)
plt.ylabel('平均耗时（秒）', fontproperties=font)
plt.ylim(min(df_mpi4py_4['平均耗时（秒）']) * 0.8, max(df_mpi4py_4['平均耗时（秒）']) * 1.2)  # 调整纵坐标范围
plt.legend(prop=font)
plt.grid(True)
plt.show()

# 绘制使用 mpi4y 且数据规模皆为 10000 的条形图
plt.figure(figsize=(12, 6))
plt.bar(df_mpi4py_10000['进程数'].astype(str), df_mpi4py_10000['平均耗时（秒）'], label='mpi4y')
plt.title('使用 mpi4y 且数据规模皆为 10000 的平均耗时', fontproperties=font)
plt.xlabel('进程数', fontproperties=font)
plt.ylabel('平均耗时（秒）', fontproperties=font)
plt.ylim(min(df_mpi4py_10000['平均耗时（秒）']) * 0.8, max(df_mpi4py_10000['平均耗时（秒）']) * 1.2)  # 调整纵坐标范围
plt.legend(prop=font)
plt.grid(True)
plt.show()

# 绘制使用 joblib 且进程数都为 4 的条形图
plt.figure(figsize=(12, 6))
plt.bar(df_joblib_4['项目规模'].astype(str), df_joblib_4['平均耗时（秒）'], label='joblib')
plt.title('使用 joblib 且进程数都为 4 的平均耗时', fontproperties=font)
plt.xlabel('项目规模', fontproperties=font)
plt.ylabel('平均耗时（秒）', fontproperties=font)
plt.ylim(min(df_joblib_4['平均耗时（秒）']) * 0.8, max(df_joblib_4['平均耗时（秒）']) * 1.2)  # 调整纵坐标范围
plt.legend(prop=font)
plt.grid(True)
plt.show()

# 绘制使用 joblib 且数据规模皆为 10000 的条形图
plt.figure(figsize=(12, 6))
plt.bar(df_joblib_10000['进程数'].astype(str), df_joblib_10000['平均耗时（秒）'], label='joblib')
plt.title('使用 joblib 且数据规模皆为 10000 的平均耗时', fontproperties=font)
plt.xlabel('进程数', fontproperties=font)
plt.ylabel('平均耗时（秒）', fontproperties=font)
plt.ylim(min(df_joblib_10000['平均耗时（秒）']) * 0.8, max(df_joblib_10000['平均耗时（秒）']) * 1.2)  # 调整纵坐标范围
plt.legend(prop=font)
plt.grid(True)
plt.show()

# 绘制使用 multiprocessing 且数据规模皆为 10000 的条形图
plt.figure(figsize=(12, 6))
plt.bar(df_multiprocessing_10000['进程数'].astype(str), df_multiprocessing_10000['平均耗时（秒）'], label='multiprocessing')
plt.title('使用 multiprocessing 且数据规模皆为 10000 的平均耗时', fontproperties=font)
plt.xlabel('进程数', fontproperties=font)
plt.ylabel('平均耗时（秒）', fontproperties=font)
plt.ylim(min(df_multiprocessing_10000['平均耗时（秒）']) * 0.8, max(df_multiprocessing_10000['平均耗时（秒）']) * 1.2)  # 调整纵坐标范围
plt.legend(prop=font)
plt.grid(True)
plt.show()

# 绘制数据规模都为 10000 且进程数都为 4 的条形图
plt.figure(figsize=(12, 6))
plt.bar(df_all_10000_4['优化情况'], df_all_10000_4['平均耗时（秒）'], label='所有库')
plt.title('数据规模都为 10000 且进程数都为 4 的平均耗时', fontproperties=font)
plt.xlabel('优化情况', fontproperties=font)
plt.ylabel('平均耗时（秒）', fontproperties=font)
plt.ylim(min(df_all_10000_4['平均耗时（秒）']) * 0.8, max(df_all_10000_4['平均耗时（秒）']) * 1.2)  # 调整纵坐标范围
plt.legend(prop=font)
plt.grid(True)
plt.show()