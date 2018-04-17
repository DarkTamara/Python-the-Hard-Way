from sys import argv

name_of_thing, user_name, insult = argv

prompt = ">" #cuz it looks cute
print "have you ever considering you are %r too hard, %r ?" %(name_of_thing, user_name)
ans1= raw_input(prompt)

print "ok, you little %r. Say smth smart?" % insult
ans2= raw_input(prompt)

print "ok. so i think i quite figured out how this works."
ans3= raw_input(prompt)

print "just to check stuff: %r , %r , %r" %(ans1, ans2, ans3)
