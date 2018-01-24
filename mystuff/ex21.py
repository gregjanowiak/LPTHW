def add(a,b):
    # print(f"ADDING {a} + {b}")
    return a + b

def subtract(a,b):
    # print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a,b):
    # print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a,b):
    # print(f"DIVIDING {a} / {b}")
    return a / b

print("let's do math with functions")

age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print(f"age: {age}\nheight: {height}\nweight: {weight}\niq: {iq}")

what = add(age,subtract(height, multiply(weight, divide(iq, 2))))

print("what is the what: ",end = "")
answer = input()

print(f"your answer: {answer}\nthe right answer: {what}")
