# Animal is-a object (look at the extra credit)
class Animal(object):
    pass

# Dog is-a Animal
class Dog(Animal):
    def __init__(self, name):
        self.name = name # Dog has-a function init and an attribute name

# Cat is-a Animal
class Cat(Animal):
    def __init__(self, name):
        self.name = name # Cat has-a attribute name

# Person is-a object
class Person(object):
    def __init__(self, name):
        self.name = name # Person has-a name attribute

# Employee is-a Person
class Employee(Person):
    def __init__(self, name, salary):
        # initialize the superclass of Employee with param name
        super(Employee, self).__init__(name)
        self.salary = salary # Employee has a salary attribute

# Fish is-a object
class Fish(object):
    pass

# Salmon is-a Fish
class Salmon(Fish):
    pass

# Halibut is-a Fish
class Halibut(Fish):
    pass

# rover is-a Dog
rover = Dog("Rover")

# satan is-a Cat
satan = Cat("Satan")

# mary is-a Person
mary = Person("Mary")

# frank is-a Employee that has-a salary of 120000
frank = Employee("Frank", 120000)

# frank has-a pet named rover
frank.pet = rover

# flipper is-a Fish
flipper = Fish()

# crouse is-a Salmon
crouse = Salmon()

# harry is-a Halibut
harry = Halibut()
