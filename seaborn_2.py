import seaborn as sns
import pandas as pd
import numpy as np
from pandas import DataFrame
import matplotlib.pyplot as plt

fig = plt.figure(dpi=100)
# plt.rc('font', family='STFangsong')
# sns.set(style="darkgrid")

base_cond = [[1, 2, 3, 4, 5, 4, 7],
             [1, 0, 3, 9, 5, 1, 7],
             [3, 2, 3, 10, 5, 9, 7],
             [1, 2, 7, 10, 4, 9, 7],
             [1, 2, 3, 6, 5, 2, 7]]

base_cond_array = np.array(base_cond)

# ============ 设置xlabel及ylabel ============
# plt.xlim(102, 48)
# x = np.linspace(100, 50, 6)
# plt.xticks(x, fontsize=11)
#
# plt.ylim(0, 1.04)
# y = np.linspace(0, 1, 11)
# plt.yticks(y, fontsize=11)

# plt.xlabel('factor', fontdict={'color': 'black',
#                              'family': 'STFangsong',
#                              'weight': 'normal',
#                              'size': 15})
# plt.ylabel('F', fontdict={'color': 'black',
#                           'fontstyle': 'italic',
#                           'family': 'Times New Roman',
#                           'weight': 'normal',
#                           'size': 15})
# ================================

# ============ 显示数据 ============
fmri = sns.load_dataset("fmri")

summary = []

for row_index in range(np.shape(base_cond_array)[0]):
    for column_index in range(np.shape(base_cond_array)[1]):
        x_t = column_index + 1
        y_t = base_cond_array[row_index, column_index]
        summary.append([x_t, y_t])

data = DataFrame(summary, columns=['factor', 'signal'])
# ================================

# 在图上绘制节点
# sns.scatterplot(x="品质因子",
#                 y="signal",
#                 data=data)
# 在图上绘制线段
sns.lineplot(x="factor",
             y="signal",
             ci='sd',
             # hue="region",
             data=data)

plt.show()
