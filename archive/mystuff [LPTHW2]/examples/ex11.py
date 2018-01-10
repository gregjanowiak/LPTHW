print "How old are you in years?", #comma lets the user input data right next to the question, instead of on a new line
age = str(raw_input()) + " years"
#str wraps the input in a string for formatting later
print "How tall are you in centimeters?",
height = str(raw_input()) + "cm"
#each statement concatenates a unit onto the input
print "How much do you weigh in kilograms?",
weight = str(raw_input()) + "kg"

print "So you're %s old, %s tall, and %s heavy." % (age, height, weight)
