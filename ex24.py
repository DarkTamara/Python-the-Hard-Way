print "let's practice... everything"
print "you\'d need to know\'bout escaping with \\ that do\n newline and \t tabs"
# the use of \ <-- dash
poem= """
\t the lovely world
with logic so firmly planted
cannot descern \n the need of love
nor comprehend passion for intuition
and requires an explanation
\n\t\twhere there is none.
""" #triple quotes op lets ya string as fk

print "----------------"
print poem
print "----------------"

five = 10 - 2 + 3 - 6 #math.jpg
print "this should be five %s" %five #lets ya format strings

def secret_formula(started): #functions stuff
    jelly_beans = started * 500 #plot twist, this stuff arae variables as well
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point) #will take the 3 values and put then in the 3 vars before =

print "with a starting point of: %d" %start_point
print "we'd have %d beans, %d jars, and %d crates." %(beans, jars, crates)

start_point = start_point / 10

print "we can also do taht this way:"
print "we have %d beans, %d jars and %d crates." %secret_formula(start_point)
