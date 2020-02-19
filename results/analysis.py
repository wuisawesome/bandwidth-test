import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression

import sys

assert len(sys.argv) == 2, "Usage: python3 analysis.py <times.txt>"

tokens = [x.split(' ') for x in open(sys.argv[1], "r").readlines()]
data = [(int(x[0]), float(x[1])) for x in tokens]

arr = np.array(data)
x = arr[:, 0].reshape(-1,1)
x = x // 2**10
y = arr[:, 1].reshape(-1,1)

model = LinearRegression().fit(x, y)

plt.plot(x, y, 'rx')
plt.show()



