formatter = "%r %r %r %s"

print formatter % (1, 2, 3, 4)
print formatter % ("one", 'two', 'three', 'four')
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter )
#this double quotation happens because i used both simple and double
# to eliminate the '' when actually printing, use %s
print formatter % (
       'i had this string',
       'that you could type up right',
       "but it didn't",
       'so i said goodnight'
)
