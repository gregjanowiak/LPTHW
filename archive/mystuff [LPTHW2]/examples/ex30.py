people = 30
cars = 40
trucks = 15

#all if statements terminate upon executing an action after a TRUE

#evaluates cars against people
if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."

#evaluates trucks against cars
if trucks > cars:
    print "That's too many trucks."
elif trucks < cars:
    print "Maybe we could take the trucks."
else:
    print "We still can't decide."

#evaluates people against trucks
if people > trucks:
    print "Alright, let's just take the trucks."
else:
    print "Fine, let's stay home then."
