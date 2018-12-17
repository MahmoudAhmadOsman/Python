#After you Download the STYLE Lib by using: pip install style
#import the stle library now

from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')

x = [5,8,10,16]
y = [12,16,6,13]

x2 = [6,9,11]
y2 = [6,15,7]

# You can plot specifically, after just showing the defaults:
plt.plot(x,y,linewidth=2) #the width and the thinkness of the graphic lines
plt.plot(x2,y2,linewidth=2) #the width and the thinkness of the graphic lines

plt.title('Mahmoud\' Plot Graph')
plt.ylabel('Y Axis')
plt.xlabel('X Axis')

plt.show() #Built in function