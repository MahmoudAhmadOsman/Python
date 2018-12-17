#Read text from a File specially csv
from matplotlib import pyplot as plt
from matplotlib import style
style.use('ggplot')
import matplotlib.collections as collections

# First, you need to import the numpy library
import numpy as np



# Create two variable to be plotted for the values in the text file
#Now, use the loadtext function
x,y = np.loadtxt(
    'readFile.csv',
    unpack=True,
    delimiter = ','
)
plt.plot(x,y)


plt.title('Data From A Text File \n Using loadtxt () function')
plt.ylabel('Y axis')
plt.xlabel('X axis')



#Then, show
plt.show()