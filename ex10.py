print "I am 6'2\" tall." # escape double- quote inside string
print 'I am 6\'2" tall.' # escape single- quote inside string
#or just use the three quotes, dah

tabby_cat= "\tI'm ta\fbbled in."
persian_cat= "I'm split\non a line."
backslash_cat= "I'm\\a\\cat."

fat_cat= """
       I'll do a list:
       \t* Cat food
       \t* Fishes
       \t* Catnip\n\t* Grass
       """
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

x= 'poop.jpg'
print "this is your face = %s" % x
