print("This is a truth table exercise, press ENTER to begin.")
input()

last_response = "False"

def truth_checker(answer, response):
    if str(answer.split(0)) == response:
        print("Correct!\n")
    else:
        print("Incorrect..\n")

print("What is: 'not False'")
last_response = input()
truth_checker(not False,last_response)

print("What is: 'not True`'")
last_response = input()
truth_checker(not True,last_response)
