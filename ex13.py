from sys import argv
# import python askes you to say what you plan to use
#keeps the program small

#argv is argument variable
#it holds the argument you pass to your python script

#the line under unpacks argv

input = raw_input('testing stuff\n')
script,first, second, third, this, that, more, maybe = argv
print "Testing stuff variable: ", input
print 'this script is called', script
print 'your first variable is:', first
print 'your second variable is:', second
print 'your third variable is', third
print 'stuff is', more
print 'something', this
print 'shalalalal',that
print 'blabla blaaa',maybe

#testing ground
