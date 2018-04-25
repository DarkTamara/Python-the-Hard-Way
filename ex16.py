from sys import argv

script, filename =argv

print "we're going to erase %r" %filename
print "if you don't want that, hit CTRL-C (^C)"
print "if you do want that, hit return"

raw_input("?")

print "opening the file..."#fake buffering message
target=open(filename, "w") #the file is opened and assigned a variable

print "truncating the file."
target.truncate() #empties the file

print "now i'll ask you for three lines."

line1 =raw_input("line 1:") #asks for the lines
line2 =raw_input("line 2:")
line3 =raw_input("line 3:")

print "i'm going to write these to the file."
target.write(line1+ "\n"+ line2+ "\n"+ line3+ "\n")
#target.write("\n") #without this it writes them one after another
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

print "And finally, we close it."
target.close()
#it has now created a .py file with the new line si wrote
