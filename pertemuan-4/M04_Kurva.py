print("\033c")

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-4, 4, num=10000)
plt.figure(figsize=(8, 6.5))

# Misal terdapat titik (-2, 0), (1, 0), dan (3, 0). Jika dimasukkan ke dalam rumus, maka 3 titik tersebut merupakan titik potong dari kurva
# y = (x + 2)(x - 1)(x - 3)
# y = x^3 - 2x^2 - 5x + 6

# Format persamaan
# y = ax^3 + bx^2 + cx + d

y = x - x - 0
y1 = x**3 - 2*x**2 - 5*x + 6

plt.plot(x, y, '-k')
plt.plot(x, (0.1 - (x - 0.1)**2)**0.5, '-k')
plt.plot(x, -(0.1 - (x - 0.1)**2)**0.5, '-k')

plt.plot(x, y1,'-r', label='y1, y2')

plt.legend(loc='upper left')
plt.grid()
plt.show()
