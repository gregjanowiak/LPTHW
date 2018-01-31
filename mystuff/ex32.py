the_count = [1,2,3,4,5]
fruits = ['apples','oranges','pears','apricots']
change = [1,'pennies',2,'dimes',3,'quarters']

#  for-loop that goes through a list
for number in the_count:
    print(f"This is count {number}")

# same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# can also iterate through mixed lists
for i in change:
    print(f"I got {i}")

# can also build lists
elements = []

# use the range to do 0-5 counts
for i in range(0,6):
    print(f"Adding {i} to the list.")
    elements.append()

for i in elements:
    print(f"Element was: {i}")
