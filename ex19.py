def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "you have %d cheese!" %cheese_count
    print "you have %d boxes of crackers" %boxes_of_crackers
    print "man that's enough to party!"
    print "get a blanket.\n"
#this defines a function and tells it what she dose and what is the name of it's arguments
#the arguments name is irelevant except for the inside of the def stuff
#they are two and will this tells the program there are 2 arguments possible
print "we can just give the function numbers directly:"
cheese_and_crackers(20, 30)
#prints the function and tells it that it's arguments are numbers

print "or, we can just use variables from our script:"
amount_of_cheese = 10 #def some variables
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)
#the variables i assigned are the arguments
print "we can even do math inside too:"
cheese_and_crackers(10+20, 5+6)
#it can do math
print "and we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 100)
#it can do more math

def mybaby(irr1, irr2,irr3):
    print "%s" %irr1
    print "%s" %irr2
    print "%s" %irr3
    
print "here we go:"
this1=raw_input("irr1=")
this2=raw_input("irr2=")
this3=raw_input("irr3=")
mybaby( this1 , this2 , this3 )
