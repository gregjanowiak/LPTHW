#not sure what to import yet

#global variables for time and cost, set to initial 0
cost = 0
time = 0
cost_limit = 300
time_limit = 3
#start = raw_input("Select SFO or LAX: ")

# write function that checks cost and time limits, return true or false
class Airport(object):
    def enter(self):
        pass

    def limitChecker(self, cost, time):

        global cost_limit
        global time_limit

        self.cost = cost
        self.time = time

        if (self.cost > cost_limit) or (self.time > time_limit):
            return 'violation'
        else:
            print "(Cost and time within limits)"

class Engine(object):
    def __init__(self, airport_map):
        self.airport_map = airport_map

    def fly(self):
        current_airport = self.airport_map.origin_airport()
        last_airport = self.airport_map.next_airport('arrived')

        while current_airport != last_airport:
            next_airport_name = current_airport.enter()
            current_airport = self.airport_map.next_airport(next_airport_name)

        current_airport.enter()

class Violation(Airport):
    messages = [
    "You're late! Should've flown direct...",
    "You spent way too much money."
    ]

    def enter(self): #ref line 32 from ex43
        global cost
        global time
        global cost_limit
        global time_limit
        if cost > cost_limit:
            print Violation.messages[1]
            exit(1)

        else:
            print Violation.messages[2]
            exit(1)

class SanFrancisco(Airport):
    def enter(self):
        global cost
        global time
        global cost_limit
        global time_limit
        # dialogue that gives first flight options
        print "Are you going to Denver, Las Vegas, or Chicago?"
        # raw input that sets a variable for selected option
        flight = raw_input('> ')
        # update the cost and time variables
        if flight == "Denver":
            cost += 200
            time += 2.5
            return 'DIA'

        elif flight == "Las Vegas":
            cost += 100
            time += 1.5
            return 'LAS'

        elif flight == "Chicago":
            cost += 350
            time += 4.5
            return 'ORD'
        # return the next airport based on choice

class LosAngeles(Airport):
    def enter(self):
        global cost
        global time
        global cost_limit
        global time_limit
        # dialogue that gives first flight options
        print "Are you going to Las Vegas, Denver, or Dallas?"
        # raw input that sets a variable for selected option
        flight == raw_input('> ')
        # update the cost and time variables
        if flight == "Las Vegas":
            cost += 100
            time += 1.5
            return 'LAS'

        elif flight == "Denver":
            cost += 200
            time += 3
            return 'DIA'

        elif flight == "Dallas":
            cost += 300
            time += 3.5
            return 'DFW'
        # return the next airport based on choice

class LasVegas(Airport):
    def enter(self):
        global cost
        global time
        global cost_limit
        global time_limit
        # dialogue that gives first flight options and current cost/time
        print "Welcome to Vegas!"

        #calls limitChecker to decide whether to continue or end as violation
        self.limitChecker(cost, time)

        print """Current travel time is: %d\n
        Incurred costs are: %d\n
        Will you be stopping in Chicago next, or going straight to Boston?
        """ % (time, cost)
        # raw input that sets a variable for selected option
        flight = raw_input('> ')
        # update the cost and time variables
        if flight == "Chicago":
            cost += 200
            time += 3
            return 'ORD'

        elif flight == "Boston":
            cost += 400
            time += 4.5
            return 'BOS'

class Denver(Airport):
    def enter(self):
        global cost
        global time
        global cost_limit
        global time_limit
        # dialogue that gives first flight options and current cost/time
        print "Welcome to Denver!"

        #calls limitChecker to decide whether to continue or end as violation
        self.limitChecker(cost, time)

        print """Current travel time is: %d\n
        Incurred costs are: %d\n
        Will you be stopping in Minneapolis next, or going straight to DC?
        """ % (time, cost)
        # raw input that sets a variable for selected option
        flight = raw_input('> ')
        # update the cost and time variables
        if flight == "Minneapolis":
            cost += 300
            time += 3
            return 'MIP'

        elif flight == "DC":
            cost += 450
            time += 4.5
            return 'IAD'

class Dallas(Airport):
    def enter(self):
        global cost
        global time
        global cost_limit
        global time_limit
        # dialogue that gives first flight options and current cost/time
        print "Welcome to Dallas!"

        #calls limitChecker to decide whether to continue or end as violation
        self.limitChecker(cost, time)

        print """Current travel time is: %d\n
        Incurred costs are: %d\n
        Will you be stopping in Atlanta next, or going straight to Boston?
        """ % (time, cost)
        # raw input that sets a variable for selected option
        flight = raw_input('> ')
        # update the cost and time variables
        if flight == "Atlanta":
            cost += 300
            time += 3
            return 'ATL'

        elif flight == "Boston":
            cost += 475
            time += 4.5
            return 'BOS'

class Chicago(Airport):
    def enter(self):
        global cost
        global time
        global cost_limit
        global time_limit
        # dialogue that gives first flight options and current cost/time
        print "Welcome to Chicago!"

        #calls limitChecker to decide whether to continue or end as violation
        self.limitChecker(cost, time)

        print """Current travel time is: %d\n
        Incurred costs are: %d\n
        Will you be going to Boston or DC next?
        """ % (time, cost)
        # raw input that sets a variable for selected option
        flight = raw_input('> ')
        # update the cost and time variables
        if flight == "Boston":
            cost += 350
            time += 3
            return 'BOS'

        elif flight == "DC":
            cost += 400
            time += 2.5
            return 'IAD'

class Minneapolis(Airport):
    def enter(self):
        global cost
        global time
        global cost_limit
        global time_limit
        # dialogue that gives first flight options and current cost/time
        print "Welcome to Minneapolis!"

        #calls limitChecker to decide whether to continue or end as violation
        self.limitChecker(cost, time)

        print """Current travel time is: %d\n
        Incurred costs are: %d\n
        Next stop, Boston!
        """ % (time, cost)

        print "Ready to go?"
        flight = raw_input('> ')

        if flight == "Yes":
            print "Here we go!"
            cost += 350
            time += 3
            return 'BOS'

        else:
            print "Okay, enjoy the cold."
            exit(1)

class Atlanta(Airport):
    def enter(self):
        global cost
        global time
        global cost_limit
        global time_limit
        # dialogue that gives first flight options and current cost/time
        print "Welcome to Atlanta!"

        #calls limitChecker to decide whether to continue or end as violation
        self.limitChecker(cost, time)

        print """Current travel time is: %d\n
        Incurred costs are: %d\n
        Next stop, Washington DC!
        """ % (time, cost)

        print "Ready to go?"
        flight = raw_input('> ')

        if flight == "Yes":
            print "Here we go!"
            return 'IAD'

        else:
            print "Okay, enjoy the humidity."
            exit(1)

class Boston(Airport): #this will return 'arrived'
    def enter(self):
        global cost
        global time
        global cost_limit
        global time_limit

        self.limitChecker(cost, time)

        # give final cost/time tabulation
        print "Welcome to Boston!\n"

        print """Final travel time is: %d\nIncurred costs are: %d\n
        """ % (time, cost)

        return 'arrived'

class WashingtonDC(Airport): #this will return 'arrived'
    def enter(self):
        global cost
        global time
        global cost_limit
        global time_limit

        self.limitChecker(cost, time)

        # give final cost/time tabulation
        print "Welcome to DC!\n"

        print """Final travel time is: %d\nIncurred costs are: %d\n
        """ % (time, cost)

        return 'arrived'

class Arrived(Airport):
    def enter(self):
        print "You made it in time! (and within budget)"
        return 'arrived'

class Map(object):

    airports = {
    'SFO': SanFrancisco(),
    'LAX': LosAngeles(),
    'LAS': LasVegas(),
    'DIA': Denver(),
    'DFW': Dallas(),
    'MIP': Minneapolis(),
    'ORD': Chicago(),
    'ATL': Atlanta(),
    'IAD': WashingtonDC(),
    'BOS': Boston(),
    'violation': Violation(), #Lose/Death
    'arrived': Arrived() #Win
    }

    def __init__(self, start_airport):
        self.start_airport = start_airport

    def next_airport(self, airport_code):
        val = Map.airports.get(airport_code)
        return val

    def origin_airport(self):
        return self.next_airport(self.start_airport)

a_map = Map('SFO')
a_game = Engine(a_map)
a_game.fly()
