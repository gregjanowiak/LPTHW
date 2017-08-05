#script that takes one argument and one raw input
from sys import argv

script, x = argv

print "Hello! What is your name?",
name = raw_input()

print "That's a weird name, %s" % name
print "My name is", x
