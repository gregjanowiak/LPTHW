numbers = []

def num_counter():
    i = int(input("enter start num: "))
    stopper = int(input("enter end num: "))
    increment = int(input("enter increment: "))

    while i < stopper:
        print(f"At the top i is {i}")
        numbers.append(i)

        i += increment
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

num_counter()

print("The numbers: ")

for num in numbers:
    print(num)
