import math
from pylab import *

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from matplotlib.cbook import get_sample_data
from matplotlib._png import read_png


from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure();
ax = fig.add_subplot(111, projection='3d')
fn = get_sample_data(r"/home/orenzah/floor.png", asfileobj=False)
img = read_png(fn)
x, y = ogrid[0:img.shape[0], 0:img.shape[1]]



x_arr = [];
y_arr = [];
z_arr = [];

powers = open('power.csv', 'r');
coors = open('Ypos.csv','r');
mini = 1;
cnt = 0;
powers.readline()
coors.readline()
for line in powers:
    arr = line.split(",");
    arr = [x.strip() for x in arr]
    power = [float(arr[0]), 10*math.log10(float(arr[1]))]
    for line_pos in coors:
        pos = line_pos.split(",");
        pos = [float(x.strip()) for x in pos]
        if pos[1] == 750 and pos[2] == 300:
            continue;
        temp = abs(power[0] - pos[0]);
        if power[0] - pos[0] < 3.0e-03:
            x_arr.append(pos[1])
            y_arr.append(pos[2])
            z_arr.append(power[1])

            #print [power[0], power[1], pos[1], pos[2]]
            break;
print mini
print cnt
print 2*math.pow(10,-10)
ax.plot(x_arr, y_arr, z_arr, label='parametric curve',facecolors=img)

plt.show()
        

