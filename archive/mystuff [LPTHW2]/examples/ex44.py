class Parent(object):
    def testing(self):
        print "This is Parent."

class Child(Parent):
    def testing(self):
        print "This Child."
        # calls super on Child, then runs testing function on what was returned (i.e. Parent)
        super(Child, self).testing()
        print "No, this is Child!"

dad = Parent()
son = Child()

dad.testing()
son.testing()
