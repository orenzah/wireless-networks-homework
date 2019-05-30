import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter, FormatStrFormatter
import matplotlib.ticker as ticker

path_diff1 = 150.0;
phase_diff1 = math.pi / 3;
amp_diff1 = 2.0;
path_diff2 = 300.0;
phase_diff2 = math.pi / 2;
amp_diff2 = 2.0;

freqs = np.arange(113000000,118000000,100)

def recv_amp(freq,phase_diff,path_diff,amp_diff):
    delay = path_diff/(3*math.pow(10,8))
    return math.sqrt(1 + math.pow(10, -amp_diff/10)+2*math.pow(10, -amp_diff/20)*math.cos(-2*math.pi*freq*delay+phase_diff))
def recv_amp_3ray(freq,phase_diff1,path_diff1,amp_diff1,phase_diff2,path_diff2,amp_diff2):
    delay1 = path_diff1/(3*math.pow(10,8))
    delay2 = path_diff2/(3*math.pow(10,8))
    ray1_cos  = math.pow(10,-amp_diff1/10)*math.cos(-2*math.pi*freq*delay1+phase_diff1);
    ray2_cos  = math.pow(10,-amp_diff2/10)*math.cos(-2*math.pi*freq*delay2+phase_diff2);
    ray1_sin  = math.pow(10,-amp_diff1/10)*math.sin(-2*math.pi*freq*delay1+phase_diff1);
    ray2_sin  = math.pow(10,-amp_diff2/10)*math.sin(-2*math.pi*freq*delay2+phase_diff2);
    return math.sqrt(math.pow(1+ray1_cos+ray2_cos,2)+math.pow(+ray2_sin,2))

y1 = np.array([recv_amp(freq,phase_diff1,path_diff1,amp_diff1) for freq in freqs])
y2 = np.array([recv_amp_3ray(freq,phase_diff1,path_diff1,amp_diff1,phase_diff2,path_diff2,amp_diff2) for freq in freqs])
fig1, ax1 = plt.subplots();

scale_x = 1e6
ticks_x = ticker.FuncFormatter(lambda x, pos: '{0:g}'.format(x/scale_x))
ax1.xaxis.set_major_formatter(ticks_x )
ax1.set_xlabel('Frequency (MHz)')

plt.grid()
plt.plot(freqs,y1)
fig2, ax2 = plt.subplots();
ticks_x = ticker.FuncFormatter(lambda x, pos: '{0:g}'.format(x/scale_x))
ax2.xaxis.set_major_formatter(ticks_x )
ax2.set_xlabel('Frequency (MHz)')
plt.plot(freqs,y2)
plt.grid()


plt.show()
