print("\033c")
import matplotlib.pyplot as plt
import numpy as np

ya = 200; xa = 200
yb = 200; xb = 600
yc = 600; xc = 200
yd = 200; xd = 200
yc = 200; xc = 100
yd = 1000; xd = 100

# points(vertex) diameter and color
pd = int(50); pr = 255; pg = 0; pb = 255

# line width and color
lw = int(50); lr = 255; lg = 0; lb = 255

col = int(1200)
row = int(1200)

def buat_garis(y1, x1, y2, x2, pd, lw, pr, pg, pb, lr, lg, lb):
    Gambar = np.zeros(shape=(row, col, 3), dtype=np.uint8)
    hd = int(pd/2) # half point diameter
    hw = int(lw/2) # half line width
    dy = y2-y1
    dx = x2 - x1
    # if (dx == 0):
    #     dx = x1

    print(f"dx = {dx}")
    print(f"dy = {dy}")

    # Draw the first point
    for i in range(x1 - hd, x1 + hd):
        for j in range(y1 - hd, y1 + hd):
            if ((i - x1) ** 2 + (j - y1) ** 2) < hd ** 2:
                Gambar[j, i, 0] = pr
                Gambar[j, i, 1] = pg
                Gambar[j, i, 2] = pb

    # Draw the second point
    for i in range(x2 - hd, x2 + hd):
        for j in range(y2 - hd, y2 + hd):
            if ((i - x2) ** 2 + (j - y2) ** 2) < hd ** 2:
                Gambar[j, i, 0] = pr
                Gambar[j, i, 1] = pg
                Gambar[j, i, 2] = pb

    # Draw the line. Untuk garis yang cenderung horizontal
    if dx != 0 and dy <= dx:
        print('HORIZONTAL')
        my = dy / dx
        for i in range(x1, x2):
            j = int(my * (i-x1) + y1)
            x = i
            y = j
            
            for i in range(x-hw, x+hw):
                for j in range(y-hw, y+hw):
                    if ((i-x) ** 2 + (j-y) ** 2) < hw ** 2:
                        Gambar[j, i, 0] = lr
                        Gambar[j, i, 1] = lg
                        Gambar[j, i, 2] = lb

    # Draw the line. Untuk garis yang cenderung vertikal
    if dx == 0 or dy > dx:
        print('VERTIKAL')
        # mx = dx / dy
        # mx = 0
        print('y1=', y1)
        print('y2=', y2)

        step = 1
        if (y1 > y2):
            step = -1

        for j in range(y1, y2, step):
            # j = int(mx * (j-y1) + x1)
            x = x1
            y = j
            
            for i in range(x-hw, x+hw):
                for j in range(y-hw, y+hw):
                    if ((i-x) ** 2 + (j-y) ** 2) < hw ** 2:
                        Gambar[j, i, 0] = lr
                        Gambar[j, i, 1] = lg
                        Gambar[j, i, 2] = lb

    return Gambar

# MAIN PROGRAM
hasil2 = buat_garis(yc, xc, yd, xd, pd, lw, pr, pg, pb, lr, lg, lb)

plt.figure()
# plt.imshow(hasil)
plt.imshow(hasil2)

plt.show()
