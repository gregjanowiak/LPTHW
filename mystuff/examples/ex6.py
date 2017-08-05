#sets 4 variables
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

#prints the output of variable x, then y on next line
print x
print y

#prints a custom string, and then raw output of x
print "I said: %r" % x
#prints a custom string, and then raw output of y
print "I also said: '%s'." % y

#sets variable to false boolean value
hilarious = False
#sets joke_evaluation variable to include custom string and a format operator for raw output
joke_evaluation = "Isn't that joke so funny?! %r"

#prints joke_evaluation and matches the hilarious variable to the included raw output format operator
print joke_evaluation % hilarious

#sets two variables
w = "This is the left side of..."
e = " a string with a right side."

#concatenates two variables
print w + e
