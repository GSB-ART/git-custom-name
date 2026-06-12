# 一个参数 默认起点0，步长为1 输出：[0 1 2 3 4 5]
import numpy as np
a = np.arange(5)
print(a)
 # 两个参数 默认步长为1 输出[3 4 5]
a = np.arange(3,6)
print(a)
# 三个参数 起点为0，终点为3，步长为0.5 输出[ 0.   0.5   1.   1.5   2.   2.5]
a = np.arange(0, 3, 0.5)
print(a)