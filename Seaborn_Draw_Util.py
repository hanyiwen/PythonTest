import seaborn as sns
import numpy as np
from pandas import DataFrame
import matplotlib.pyplot as plt


# list1, list 应该为二维数组的坐标
def draw_twin_pic(list1, list2, x_label, left_y_label, right_y_label, x_legend, y_legend,
                  x_legend_location,y_legend_location, line1_color, line2_color):
    # fig = plt.figure(dpi=150)
    fig = plt.figure(figsize=(9,8))
    ax1 = fig.add_subplot(111)
    ax2 = ax1.twinx()  # this is the important function

    ax1.axes.set_ylabel(left_y_label, fontdict={'size': 15})
    ax1.axes.set_xlabel(x_label, fontdict={'size': 15})
    ax2.axes.set_ylabel(right_y_label, fontdict={'size': 15})

    base_cond_array1 = np.array(list1)
    base_cond_array2 = np.array(list2)


    # ============ 显示数据 ============

    summary1 = []
    summary2 = []

    for row_index in range(np.shape(base_cond_array1)[0]):
        for column_index in range(np.shape(base_cond_array1)[1]):
            x_t = column_index + 1
            y_t = base_cond_array1[row_index, column_index]
            summary1.append([x_t, y_t])

    for row_index in range(np.shape(base_cond_array2)[0]):
        for column_index in range(np.shape(base_cond_array2)[1]):
            x_t = column_index + 1
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
                 ax=ax1,label=x_legend,legend=False)
    sns.lineplot(x=x_label,
                 y=right_y_label,
                 ci='sd',
                 color=line2_color,
                 data=data2,
                 ax=ax2,label=y_legend,legend=False)
    fig.legend(loc=1, bbox_to_anchor=(1, 0.6), bbox_transform=ax1.transAxes, fontsize=12)
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

draw_twin_pic(list1=list1,
              list2=list2,
              x_label='Iteration Time',
              left_y_label='Overall Experience Loss',
              right_y_label='The Number of Beneficial\n Offloading Players',
              x_legend='Experience Loss',
              y_legend='Beneficial Number',
              x_legend_location='center right',
              y_legend_location='center right',
              line1_color='blue',
              line2_color='green'
              )
