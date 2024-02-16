fileObj  = open("Incubators.txt","r+")

#Tell are  starting main character of line
print(fileObj.tell())

#Reading the content from a particular position to end of the file
print(fileObj.read())

#last character no of line
print(fileObj.tell())