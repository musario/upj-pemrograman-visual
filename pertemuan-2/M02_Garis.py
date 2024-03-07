import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10)
plt.figure(figsize=(5, 15))
print(x)

y1 = x
y2 = x - x - 0
y3 = x*0.5
y4 = (-x**2 + 100)
y5 = (x**2 - 100)

r = np.array([10])
# y6 = np.pi * r ** 2

plt.plot(x, y1, '-r', label='y1')
# plt.plot(x, y2, '-k', label='y2')
plt.plot(x, y3, '-g', label='y3')
plt.plot(x, y4, '-b', label='y4')
plt.plot(x, y5, '-m', label='y5')
# plt.plot(x, y6, '-c', label='y6')
plt.legend(loc='upper left')
plt.grid()
plt.show()
