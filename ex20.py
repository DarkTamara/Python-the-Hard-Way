from sys import argv
#will need to give it the name of the file
script, input_file = argv

def print_all(f):#defines this to read a argument that is a file
    print f.read()

def rewind(f):
    f.seek(0) #sets the file's current position at the offset

def print_a_line(line_count, f): #defines this to read line
    print line_count, f.readline() #you’re reading a line from the file and moving the read head to right
                                   #after the\n that ends that file

current_file = open(input_file) # puts the file in a var

print "first let's print the whole file: \n"
print_all(current_file) # prints the file cuz the function argument is a string in witch is he file

print "now let's rewind, kind of like a tape"
rewind(current_file)
#shit hits fan
print "let's print three lines:"

current_line = 1 #defines a var
print_a_line(current_line, current_file) #calls on the function
#will print 1 and the first line of the file
current_line += current_line
print_a_line(current_line, current_file)
#will print 2 (1+1) and the second line
current_line = current_line + 1
print_a_line(current_line, current_file)
#will print 3 and the third line
