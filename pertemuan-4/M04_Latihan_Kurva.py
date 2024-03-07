print("\033c")

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, num=10000)
plt.figure(figsize=(8, 6.5))

# (-1, 0), (1, 0), (2, 0)

# y = (x + 1) * (x - 1) * (x - 2)
# y = x^2 - 1 * (x - 2)
# y = x^3 - 2x^2 - x + 2

y = x - x - 0
y1 = -(x**3 - 2*x**2 - x + 2)

plt.plot(x, y, '-k')

plt.plot(x, y1,'-r', label='y1, y2')

plt.legend(loc='upper left')
plt.grid()
plt.show()
