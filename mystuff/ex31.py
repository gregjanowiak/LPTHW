print("""You enter a dark toom with two doors.
Do you go through door 1 or door 2?""")

door = input("> ")

if door == "1":
    print("There's a giant bear eating a cheese cake.")
    print("What do you do?")
    print("1. take the cake")
    print("2. scream at the bear")

    bear = input("> ")

    if bear == "1":
        print("the bear ate your face, good job!")
    elif bear == "2":
        print("the bear ate your legs off, good job!")
    else:
        print(f"well, doing {bear} is probably better")
        print("(bear runs away)")

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")

else:
    print("You stumble around and fall on a knife and die.  Good job!")
