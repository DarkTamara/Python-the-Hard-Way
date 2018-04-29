def add(a,b): #a function with 2 arguments
    print "adding %d + %d" % (a, b)
    return a + b

ask1 = float(raw_input("Age?")) #modificari nebunesti ca sa raw_input
age = add (ask1, 5) #will add the arguments, here ints

print "age:%d" % age
