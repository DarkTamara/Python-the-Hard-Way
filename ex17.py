from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "copying from %s to %s" %(from_file, to_file)

#do this two in one
in_file = open(from_file, "r") #opens the stuff
indata = in_file.read() #assigns the stuff to a variable
#tells me how big the file is
print "the input file is %d bytes long" %len(indata)
#it veryfies if the file exists, returns true if it is
print "dose the output file exist ? %r" %exists(to_file)
print "ready, hit enter to continue, ctrl-c to abort."
raw_input()

out_file = open(to_file, "w") #opens the file
out_file.write(indata)  #writes a file with the info from indata avriable
print "alright, all done."

out_file.close() #closes the file
in_file.close()  #same
