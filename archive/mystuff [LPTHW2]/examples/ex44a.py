class Parent(object):

    def override(self):
        print "PARENT override"


    def implicit(self):
        print "PARENT implicit"


    def altered(self):
        print "PARENT altered"


class Child(Parent):

    def override(self):
        print "CHILD override"


    def altered(self):
        print "CHILD altered"
        super(Child, self).altered()
        print "No, CHILD altered!"

dad = Parent()
son = Child()

dad.override()
dad.implicit()
dad.altered()
print "\n"
son.override()
son.implicit()
son.altered()
