name = 'zed a shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
height_cm = height * 2.54
weight_kg = weight * 0.453592
eyes = 'blue'
teeth = 'white'
hair = 'brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall")
print(f"(that's {height_cm} in cm)")# convert to cm
print(f"He's {weight} pounds heavy")
print(f"(that's {weight_kg} in kg)")# convert to kg

total = age + height + weight
print(f"If we add {age}, {height}, and {weight} we get {total}.")
