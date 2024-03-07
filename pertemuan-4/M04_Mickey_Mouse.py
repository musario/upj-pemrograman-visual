print("\033c")

import numpy as np
import matplotlib.pyplot as plt

# y = b +- (r - (x - a)**2)**0.5

# Domain
r_head = 5
r_ear = 2

x = np.linspace(-9, 9, num=10000)
plt.figure(figsize=(8, 6.5))

# y = x -x -0

# (5, 5)
y1 = 5 + (r_head - (x - 5)**2)**0.5 
y2 = 5 - (r_head - (x - 5)**2)**0.5

# (3, 7)
y3 = 7 + (r_ear - (x - 3)**2)**0.5
y4 = 7 - (r_ear - (x - 3)**2)**0.5
    
# (7, 7)
y5 = 7 + (r_ear - (x - 7)**2)**0.5
y6 = 7 - (r_ear - (x - 7)**2)**0.5

plt.plot(x, y1,'-k', label='y1,y2')
plt.plot(x, y2,'-k')
plt.fill_between(x, y1, y2, color='black')

plt.plot(x, y3,'-k', label='y1,y2')
plt.plot(x, y4,'-k')
plt.fill_between(x, y3, y4, color='black')

plt.plot(x, y5,'-k', label='y1,y2')
plt.plot(x, y6,'-k')
plt.fill_between(x, y5, y6, color='black')

plt.show()
