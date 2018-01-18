# simple text editor

from sys import argv

script,filename = argv

print(f"We're going to erase {filename}")
print("If you don't want that, hit ctrl-c")
print("If you do want that, hit RETURN")

input("?")

print("Truncating the file now...")
target = open(filename,'w')

print("Now I'll ask for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("Writing these to the file...")

target.write(f"{line1}\n{line2}\n{line3}\n")

print("Now closing the file.")
target.close()
