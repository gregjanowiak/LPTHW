#like scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

#last one was actually pointless
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

#this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

#this one takes no arguments
def print_none():
    print "I got nothin'."

#runs all of the previously defined functions
print_two("Greg", "Janowiak")
print_two_again("Greg", "Janowiak")
print_one("First!")
print_none()
