def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d + %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

#formula for the nested functions in previous script
puzzle = age + (height - (weight * (iq / 2)))
print '''
Original puzzle answer should be "-4391"\n
You got %d
''' % puzzle

print "Now for a new puzzle!"

#new formula and nested function pair
puzzle2 = age * (height + (weight - iq)) / 3
puzzle3 = multiply(age, add(height, subtract(weight, iq))) / 3

print "and the moment of truth..."
raw_input("(Press ENTER to check answer)")
print "computer's value = %d" % puzzle2
print "your hopefully matching value = %d" % puzzle3

print "\nDid you get it right? (Y or N)"
answer = raw_input("> ")

if answer is "Y":
    print "Great job!"
else:
    print "Aww, maybe next time"
