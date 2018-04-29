def add(a,b): #a function with 2 arguments
    print "adding %d + %d" % (a, b)
    return a + b

def subtract(a,b):#a function with 2 arguments
    print "subtracting %d - %d" %(a, b)
    return a - b

def multiply(a,b):#a function with 2 arguments
    print "multiply %d * %d" %(a, b)
    return a * b

def divide(a,b):#a function with 2 arguments
    print "divide %d / %d" %(a,b)
    return a / b

print "let's do some math just functions!"

ask1 = float(raw_input("Age?")) #modificari nebunesti ca sa raw_input
age = add (ask1, 5) #will add the arguments, here ints
ask2 = float(raw_input("height?"))
height = subtract(ask2, 4)
ask3 = float(raw_input("weight?"))
weight = multiply(ask3, 2)
ask4 = float(raw_input("iq?"))
iq = divide(ask4, 2)
#prints them
print "age:%d \n height: %d \n weight %d \n IQ: %d " % (age,height,weight,iq)

#puzzle stuff
print "here is a puzzle"
what= add(age, subtract(height, multiply(weight, divide(iq,2))))
#will divide iq by 2, then multiply by the weight and then from the height it will
# substract that, and then it will and the age
print "that becomes:", what, "can you do it by hand?"
