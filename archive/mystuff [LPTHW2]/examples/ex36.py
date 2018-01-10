from sys import exit

#define first room
def bad_room():
    print "You're pretty screwed, so pick a hand (left or right)"

    choice = raw_input("> ")

    if "left" in choice:
        dead("Ohh that's not correct.")
    elif "right" in choice:
        dead("Yikes, shouldn't have picked that one.")
    else:
        dead("Yeah, that wasn't an option. Bye!")

#define second room
def worse_room():
    print "There's no way out! What next? (Hint: say 'please')"

    choice = raw_input("> ")

    if "please" in choice:
        dead("Why would you listen to me???")
    else:
        print "Hey you're mean! I'm leaving! Hope you feel better about yourself!"
        exit(0)

#define start sequence
def start():
    print "Welcome to GregLand!"
    print "Please choose a door! (1 or 2)"

    choice = raw_input("> ")

    if choice == '1':
        bad_room()
    elif choice == '2':
        worse_room()
    else:
        dead("You won the game! I don't know what to say, so I guess\n")

#define dead function
def dead(reason):
    print reason, "wamp wamp wahhh..."
    exit(0)

start()
