#Math lab BAR Graph


from matplotlib import pyplot as plt
from matplotlib import style


#ggplot is a plotting system for Python
style.use('ggplot')


x = [5,8,10]
y = [12,16,6]

x2 = [6,9,11]
y2 = [6,15,7]



#Call the bar() function in order to use the bar graph
plt.bar(x,y, align='center', color='#db1abb')


#Now, show the x2 and y2 plots on the graph
plt.bar(x2,y2, color='#db1a61', align='center')

#Also, you can add Labels for X and Y and Title

plt.title("Mahmoud\'s Bar Graph")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")


plt.show()