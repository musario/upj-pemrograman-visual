print("\033c")

import numpy as np
import matplotlib.pyplot as plt

# Domain
x = np.linspace(-8, 8, num=10000)
plt.figure(figsize=(8, 6.5))

# Rumus
# y = b +- (x - (x - a)**2)**0.5

d = 16
r = d/2

# Persamaan matematika

# (range, 0)
y = x -x -0

# (0, 0)
y1 = (r - x**2)**0.5
y2 = -(r - x**2)**0.5

# (5, 5)
y3 = 5 + (r-(x-5)**2)**0.5
y4 = 5 - (r-(x-5)**2)**0.5

# (-5, -5)
y5 = -5 + (r-(x+5)**2)**0.5
y6 = -5 - (r-(x+5)**2)**0.5

# (-5, 5)
y7 = 5 + (r-(x+5)**2)**0.5
y8 = 5 - (r-(x+5)**2)**0.5

# (5 , -5)
y9 = -5 + (r-(x-5)**2)**0.5
y10 = -5 - (r-(x-5)**2)**0.5

plt.plot(x, y, '-k')
plt.plot(x, y1,'-r', label='y1,y2')
plt.plot(x, y2,'-r')
plt.plot(x, y3,'-g', label='y3,y4')
plt.plot(x, y4,'-g')
plt.plot(x, y5,'-b', label='y5,y6')
plt.plot(x, y6,'-b')
plt.plot(x, y7,'-y', label='y7,y8')
plt.plot(x, y8,'-y')
plt.plot(x, y9,'-m', label='y9,y10')
plt.plot(x, y10,'-m')

plt.legend(loc='upper center')
plt.grid()
plt.show()

