# reads a file

from sys import argv

script,filename = argv

target = open(filename)

print("Here is the contents of {filename}:")

target.read()
