#Using the File Write Method
#One thing you’ll notice about the file write method is that it only requires a single parameter, which is the string you want to be written.
#1st open the file by using open () function with the mode 'w' for writing
writetotext = open('writetotext.txt', 'w')

#Now, write a text to the file by using the write() function
writetotext.write("This is the new text that I just wrote to the file")
writetotext.write("Another new text")

#pring the text in the file by using for loop
for linetext in writetotext:
    print(writetotext.readlines())

writetotext.close()