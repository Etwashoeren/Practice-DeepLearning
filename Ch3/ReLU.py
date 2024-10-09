import numpy as np
from matplotlib import pyplot as plt


def relu(x):
    return np.maximum(x, 0)

x = np.arange(-6, 6, 0.1)
y = relu(x)
plt.plot(x, y)
plt.ylim(-1, 5)
plt.show()