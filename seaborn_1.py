import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# base_cond = [[18, 20, 19, 18, 13, 4, 1],
#              [20, 17, 12, 9, 3, 0, 0],
#              [20, 20, 20, 12, 5, 3, 0]]
base_cond = [[1, 2, 3, 4, 5, 4, 7],
             [1, 0, 3, 9, 5, 1, 7],
             [1, 2, 3, 10, 5, 9, 7]]

fig = plt.figure()

xdata = np.array([0, 1, 2, 3, 4, 5, 6]) / 5


sns.tsplot(time=xdata, data=base_cond, color='g', linestyle='-')

plt.show()

