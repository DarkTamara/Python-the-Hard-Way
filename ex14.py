from sys import argv

script, user_name =argv
prompt = '><.><'

print "Hi %s, I'm the %s script." % (user_name, script)
#by default it will take the ex14.py as first arg
#then the second one is the one you type in the comand line
print "I'd like to ask you a few questions."
print "Do you like me %s ?" % user_name
likes = raw_input(prompt)

print "Where do you live %s ?" % user_name
lives = raw_input(prompt)
#takes the answer i give and makes it a string
#also, the user_name at the end is given by me when i run teh stuff
print "In other news, how are you %s ?" %user_name
feels = raw_input(prompt)

print "Waht kind of computer do you have?"
computer = raw_input(prompt)

print """
   Alright, so you said %r about likeing me.
   You live in %r. Not sure where that is.
   And you have a %r computer.
   Also, you feel %r . Nice.
   """ %(likes, lives, computer, feels)
