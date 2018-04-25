from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "copying from %s to %s" %(from_file, to_file)

#do this two in one
in_file = open(from_file)
indata = in_file.read()

print "the input file is %d bytes long" %len(indata)
#it veryfies if the file exists, returns true if it is
print "dose the output file exist ? %r" %exists(to_file)
print "ready, hit enter to continue, ctrl-c to abort."
raw_input()

out_file = oepn(to_file, "w")
out_file.write(indata)

print "alright, all done."

out_file.close()
in_file.clsoe()
