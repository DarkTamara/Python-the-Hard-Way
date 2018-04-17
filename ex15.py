from sys import argv

script, filename = argv #cere stuff
#open() returns a file object, and is most commonly used with two arguments: open(filename, mode).
txt = open(filename)#openes the stuff i tell him to when i run it

print "here's your file %r:" %filename
print txt.read() #it tells it to read and print
#you give files comands by useing .then the comand and parameters
print "type your filename again:"
#asks for imput, and assigns the stuff to a new var
file_again= raw_input(">")

txt_again = open(file_again)

print txt_again.read()
