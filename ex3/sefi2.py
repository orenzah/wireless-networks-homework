import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter, FormatStrFormatter
import matplotlib.ticker as ticker


def ray(amplitude_diff, freq, time_diff, phase_diff):
    value = amplitude_diff*np.exp(1j*(-2*np.pi*freq*time_diff+phase_diff));    
    return value;

def rays(n,freqs):    
    R = np.ones(len(freqs), dtype='complex128')
    for i in range(n-1):
        phase_diff = np.random.random()*0.4 * np.pi;        
        time_diff = np.random.random() * math.pow(10, -6);
        amplitude_diff = np.power(10, -((2)/10))
        arr = np.array([ray(amplitude_diff, freq, time_diff, phase_diff) for freq in freqs], dtype='complex128')        
        R = np.add(R,arr)
    return np.absolute(R);

        
freqs = np.arange(113000000,118000000,100)

fig1, ax1 = plt.subplots();
y1 = rays(10000, freqs)
scale_x = 1e6
ticks_x = ticker.FuncFormatter(lambda x, pos: '{0:g}'.format(x/scale_x))
ax1.xaxis.set_major_formatter(ticks_x )
ax1.set_xlabel('Frequency (MHz)')
plt.grid()
plt.plot(freqs,y1)        
plt.show()    
    
