fileObj = open("Incubators.txt","r+")

print(fileObj.read()) # read the content of a text file

# To write into a file, we use "write()" method
fileObj.close()   # close the file after writing to it

