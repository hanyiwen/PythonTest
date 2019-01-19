import seaborn as sns
import numpy as np
from pandas import DataFrame
import matplotlib.pyplot as plt


# 画出list1, list2 两个数组双y轴的图
def draw_twin_pic(x_start, x_interval, list1, list2, x_label, left_y_label, right_y_label, x_legend, y_legend,
                  legend_loc, line1_color, line2_color):
    fig = plt.figure(dpi=100)
    ax1 = fig.add_subplot(111)
    ax2 = ax1.twinx()  # this is the important function

    ax1.axes.set_ylabel(left_y_label, fontdict={'size': 15})
    ax1.axes.set_xlabel(x_label, fontdict={'size': 15})
    ax2.axes.set_ylabel(right_y_label, fontdict={'size': 15})

    base_cond_array1 = np.array(list1)
    base_cond_array2 = np.array(list2)

    summary1 = []
    summary2 = []

    for row_index in range(np.shape(base_cond_array1)[0]):
        for column_index in range(np.shape(base_cond_array1)[1]):
            x_t = column_index * x_interval + x_start
            y_t = base_cond_array1[row_index, column_index]
            summary1.append([x_t, y_t])

    for row_index in range(np.shape(base_cond_array2)[0]):
        for column_index in range(np.shape(base_cond_array2)[1]):
            x_t = column_index * x_interval + x_start
            y_t = base_cond_array2[row_index, column_index]
            summary2.append([x_t, y_t])

    data1 = DataFrame(summary1, columns=[x_label, left_y_label])
    data2 = DataFrame(summary2, columns=[x_label, right_y_label])

    # 在图上绘制线段
    sns.lineplot(x=x_label,
                 y=left_y_label,
                 ci='sd',
                 data=data1,
                 color=line1_color,
                 ax=ax1, label=x_legend, legend=False)
    sns.lineplot(x=x_label,
                 y=right_y_label,
                 ci='sd',
                 color=line2_color,
                 data=data2,
                 ax=ax2, label=y_legend, legend=False)
    fig.legend(loc=legend_loc, bbox_to_anchor=(1, 0.6), bbox_transform=ax1.transAxes, fontsize=12)
    plt.show()


# 画出单个数组的图
def draw_single_pic(x_start, x_interval, list, x_label, left_y_label, x_legend, line1_color):
    fig = plt.figure(dpi=100)
    ax1 = fig.add_subplot(111)

    ax1.axes.set_ylabel(left_y_label, fontdict={'size': 15})
    ax1.axes.set_xlabel(x_label, fontdict={'size': 15})

    base_cond_array1 = np.array(list)

    summary1 = []

    for row_index in range(np.shape(base_cond_array1)[0]):
        for column_index in range(np.shape(base_cond_array1)[1]):
            x_t = column_index * x_interval + x_start
            y_t = base_cond_array1[row_index, column_index]
            summary1.append([x_t, y_t])

    data1 = DataFrame(summary1, columns=[x_label, left_y_label])

    # 在图上绘制线段
    sns.lineplot(x=x_label,
                 y=left_y_label,
                 ci='sd',
                 data=data1,
                 color=line1_color,
                 ax=ax1, label=x_legend, legend=False)

    plt.show()


# Main测试
list1 = [[1, 2, 3, 4, 5, 4, 7],
         [1, 0, 3, 4, 5, 6, 7],
         [3, 2, 3, 4, 5, 6, 9],
         [1, 2, 7, 10, 4, 6, 7],
         [1, 2, 3, 4, 5, 2, 7]]

list2 = [[600, 2, 300, 4, 500, 1, 7],
         [600, 5, 400, 3, 200, 1, 7],
         [600, 5, 400, 3, 200, 1, 7],
         [700, 5, 400, 3, 200, 1, 7],
         [600, 5, 400, 3, 200, 2, 7]]

draw_twin_pic(
    x_start=100,
    x_interval=30,
    list1=list1,
    list2=list2,
    x_label='Iteration Time',
    left_y_label='Overall Experience Loss',
    right_y_label='The Number of Beneficial\n Offloading Players',
    x_legend='Experience Loss',
    y_legend='Beneficial Number',
    legend_loc=1,
    line1_color='blue',
    line2_color='green'
)

draw_single_pic(
    x_start=100,
    x_interval=30,
    list=list1,
    x_label='Iteration Time',
    left_y_label='Overall Experience Loss',
    x_legend='Experience Loss',
    line1_color='blue'
)
