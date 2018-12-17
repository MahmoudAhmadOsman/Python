#Matlab Legend function
#t's important to call legend AFTER you've plotted what you want to be included in the legend.

from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')

x = [5,8,10]
y = [12,16,6]

x2 = [6,9,11]
y2 = [6,15,7]

# You can plot specifically, after just showing the defaults:
plt.plot(x,y,linewidth=2) #the width and the thinkness of the graphic lines
plt.plot(x2,y2,linewidth=2) #the width and the thinkness of the graphic lines

plt.title('Mahmoud\'s Legend Graph')
plt.ylabel('Y Axis')
plt.xlabel('X Axis')



#LEDEND function: call it after you plotting the x and y values

plt.legend()


#Also, you can add Color to the graph line
plt.grid(True,color='#d12765') #k for black or you can put hex color



plt.show() #Built in function