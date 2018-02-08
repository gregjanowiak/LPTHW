states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville',\
}

# add to cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print('-' * 10)
print("NY state has: ", cities['NY'])
print("OR state has: ", cities['OR'])

print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

print('-' * 10)
print("Michigan has: ",cities[states['Michigan']])

print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")
