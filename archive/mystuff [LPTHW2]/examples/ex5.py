name = 'Gregory M. Janowiak'
age = 24 #not a lie
height = 74.0 #inches
metric_height = height * 2.54 #centimeters
weight = 180.0 #pounds
metric_weight = weight * .4535
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall (or %g cm)." % (height, metric_height)
print "He's %d pounds heavy (or %g kg)." % (weight, metric_weight)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on how much coffee he drank." % teeth

#here comes the tricky line
print "If I add %d, %d, and %d I get %d" % (age, height, weight, age + height + weight)
