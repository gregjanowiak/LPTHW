formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
#puts the formatter inside the formatter 4 times
print formatter % (formatter, formatter, formatter, formatter)
#prints out a string of four strings
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    #displays as double quotes because of the conjunction
    "But it didn't sing.",
    "So I said goodnight."
)
