from sys import exit

def gold_room():
    print("This room is full of gold, how much do you take?")

    choice = int(input("> "))
    if choice > 0:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy. You win!")
        exit(0)
    else:
        dead("You greedy bastard!")

def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")

    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear looks at you and slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved, you can open the door")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed and eats you")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I have no idea what that means")

def cthulu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty")
    else:
        cthulu_room()

def dead(why):
    print(why,"Good job!")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulu_room()
    else:
        dead("You stumble around the room until you starve.")

start()
