import numpy as np
import matplotlib.pyplot as plt

N = 30
x = np.random.rand(N)
y = np.random.rand(N)
area = np.pi*3
plt.scatter(x, y, s=area, c='blue', alpha=0.5)
plt.title('Scatter plot')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
