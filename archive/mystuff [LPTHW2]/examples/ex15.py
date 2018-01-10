#imports the argv variable from the sys library/module
from sys import argv

#allows the script to accept an argument
script, filename = argv

file_opener = open(filename)

#uses the file_opener method to read your file from the argument above
print "Here is your file %r:" % filename
print file_opener.read()

#sets the file_collect variable equal to your raw input
print "Type the name of the file to read again:",
file_collect = raw_input('> ')

#sets the file_convert variable to the opened file contents of file_collect variable
file_convert = open(file_collect)

#prints the contents of the file object in the file_convert variable
print file_convert.read()

#closes the open files
file_opener.close()
file_convert.close()
