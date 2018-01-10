#imports argv module from sys library
from sys import argv

#script takes two arguments
script, title, user_name = argv
prompt = 'answer: '

#outputs string data from the script arguments
#takes raw input via prompt defined above
print "Hi %s %s, I'm the %s script." % (title, user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s %s?" % (title, user_name)
likes = raw_input(prompt)

print "Where do you live %s %s?" % (title, user_name)
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

#reads back all of the collected input in raw form
print '''
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
''' % (likes, lives, computer)
