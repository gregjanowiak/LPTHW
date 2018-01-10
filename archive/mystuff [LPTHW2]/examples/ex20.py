from sys import argv

script, input_file = argv

#defines a function with argument f, that reads the f object (text file)
def print_all(f):
    print f.read()

#defines a function that sets the file f current position to the beginning
def rewind(f):
    f.seek(0)

#defines a function that prints the first arg and one line of the f file
def print_a_line(line_count, f):
    print line_count, f.readline(),

current_file = open(input_file)

print "First, let's print the whole file:\n"
print_all(current_file)

print "Now let's rewind, kind of like a tape."
rewind(current_file)

#prints the first three lines of current_file
#because rewind sets to beginning
#and print_a_line reads each one in sequence as the file position moves up
print "Let's print three lines:"
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
