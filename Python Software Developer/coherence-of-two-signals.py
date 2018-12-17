import numpy as np
import matplotlib.pyplot as plt

# Fixing random state for reproducibility
np.random.seed(3657894332)

data = 0.01
time = np.arange(0, 30, data)
nse1 = np.random.randn(len(time))                 # white noise 1
nse2 = np.random.randn(len(time))                 # white noise 2

# Two signals with a coherent part at 10Hz and a random part
s1 = np.sin(2 * np.pi * 10 * time) + nse1
s2 = np.sin(2 * np.pi * 10 * time) + nse2

fig, axs = plt.subplots(2, 1)



axs[0].plot(time, s1, time, s2)


axs[0].set_xlim(0, 2)
axs[0].set_xlabel('Time')
axs[0].set_ylabel('s1 and s2')
axs[0].grid(True)

cxy, f = axs[1].cohere(s1, s2, 256, 1. / data)
axs[1].set_xlabel('Time')
axs[0].set_ylabel('COHERENCE')
axs[0].set_title('Mahmoud\'s Figure')

fig.tight_layout()
plt.show()
