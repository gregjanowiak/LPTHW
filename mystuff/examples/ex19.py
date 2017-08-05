#defines the function and arguments, prints output
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man, that's enough for a big party!"
    print "Get a blanket.\n"

#calls the function with arguments
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

#sets global variables, then calls the function using vars as args
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#calls the function with arithmetic args
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

#calls the function with hybrid args
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
