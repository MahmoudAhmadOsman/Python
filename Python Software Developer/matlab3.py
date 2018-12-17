#Importing pyplot
from matplotlib import pyplot as plt

#Plotting to our canvas
#Put x and y for each of these values
#plt.plot([1,2,3,8],[4,5,1,9])
x = [1,2,3,8]
y = [4,5,1,6]

#Now plot these numbers, using the plot() function
plt.plot(x,y)

#Also, you can add title and label for x an y. using the title() function
plt.title('Mahmoud\'s Python Graph')
plt.ylabel('Y Axis')
plt.xlabel('X Axis')


#Showing what we plotted
plt.show()