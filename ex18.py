#functions do :
#1 name pieces of code like variables do with strings
#2 take arguments like scripst take argv
#3 they let ya make a "mini-script"
#you can create a function useing def

#this one is like your script with argv
def print_two(*args): #tells python this is a function, and names it
    arg1, arg2 =args #like argv but for functions
    print "arg1: %r, arg2=%r " %(arg1, arg2)#just to see if it works

#ok, that *args is actually pointless, we can just do This
def print_again(arg1,arg2): #just uses the variables, no need to compress and decompress
    print "arg1: %r, arg2=%r " %(arg1, arg2)

#this is just one more argument
def print_one(arg1):
    print "arg1:%r" % arg1

#this one tales no arguments
def print_none():
    print "i got nothing"

print_two("zed", "shaw")
print_again("zed","shaw")
print_one("one")
print_none()
