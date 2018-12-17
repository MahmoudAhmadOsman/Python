#First step: open the file that you want to read by using open function
myfile = open('mytext.txt', 'r')

#print (myfile.read())

#read all the text in the files by using readlines() function
#print (myfile.readlines())

#use for loop and also read the test in the file
for lines in myfile:
    print(myfile.readlines())


myfile.close()