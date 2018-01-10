"I am 6'2\" tall." #escapes the inch symbol
'I am 6\'2" tall.' #escapes the foot symbol

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

#challenge code: prints weird spinny line because all conditions are True
while True:
    for i in ["/", "-", "|", "\\", "|"]:
        print "%s\r" % i,
