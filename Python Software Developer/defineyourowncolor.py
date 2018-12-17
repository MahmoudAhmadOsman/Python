import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import style
plt.style.use('ggplot')
style.use('fivethirtyeight')

x = [1,5,6,9]
y = [6,5,4,2]

v1 = [3,5,6,7]
v2 = [5,9,7,8]


plt.plot(x,y)
plt.plot(v1, v2)
plt.title('My New Graph')
plt.xlabel('This is X Axis')
plt.ylabel('This is Y Axis')
plt.bar(5,8) #where you want to point for x and y to start
#plt.tight_layout()

plt.legend('XY')
plt.show()