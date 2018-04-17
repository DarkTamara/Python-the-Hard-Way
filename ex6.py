x= 'There are %d type of people' %10
binary= "binary "
do_not= "don't"
y= "those who know %s and those who %s." % (binary, do_not) #here

print x
print y

print "i said : %r " % x # here
print "i also said: '%s'." % y #here

hilarious = False
joke_evaluation = "isn't taht joke funny ? %r "#here

print joke_evaluation %hilarious

w= 'this is the left side of...'
e= 'this is the right side.'
# as far as my brain can understand, this combines the elements of both strings
# and creates a new string with all teh elements in it
print w+e
