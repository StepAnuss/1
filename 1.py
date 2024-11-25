import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 10, 0.1)
chislitel = np.sqrt(1 + np.e ** (np.sqrt(x)) + np.cos(x ** 2))
znamen = np.abs(1 - np.sin(x) ** 3)
ostat = np.log(x)
y = (chislitel / znamen) + ostat

plt.grid()
plt.plot(x, y)
plt.fill_between(x, y)

area = np.trapezoid(y)
plt.show()
print(area)
