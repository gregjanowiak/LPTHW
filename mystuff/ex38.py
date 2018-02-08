ten_things = "apples oranges crows telephone light sugar"

print("Wait, there are not ten things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ['day','night','song','frisbee','corn','banana','girl','boy']

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", more_stuff)
    stuff.append(next_one)
    print("There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1]) # second item in stuff
print(stuff[-1]) # last item in stuff
print(stuff.pop()) # last item in stuff, removes item from list
print(' '.join(stuff)) # prints stuff as string with spaces between items
print('#'.join(stuff[3:5])) # prints stuff items 4 and 5 with # between items
