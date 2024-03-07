import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(4, 15))

# Garis Pertama
x = np.array([0, 4])
y = np.array([0, 1])
plt.plot(x, y, '-b', label='garis pertama')

# Garis Kedua
x = np.array([4, 12])
y = np.array([1, 1])
plt.plot(x, y, '-r', label='garis kedua')

# Garis Ketiga
x = np.array([12, 10])
y = np.array([1, 0])
plt.plot(x, y, '-m', label='garis ketiga')

plt.legend(loc='upper left')
plt.grid()
plt.show()
