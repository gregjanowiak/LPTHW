def loopTest(limit):

    numbers = []

    for i in range(0, limit):
        print "The list will now go up to %d" % i
        numbers.append(i)

        print "Numbers now: ", numbers, '\n'

    print "The numbers: "

    for i in numbers:
        print i
