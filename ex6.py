# define the variable x
x = "There are %d types of people." % 10
# define the variable binary
binary = "binary"
# define the variable do_not
do_not = "don't"
# define the variable y
y = "Those who know %s and those who %s." % (binary, do_not)

# print variable x
print (x)
# print variable y
print (y)

# print the string "I said %r." % x - this formats the raw data of the variable to the string
print ("I said: %r." % x)
# # print the string "I also said %s." % y - this formats the variable y to the string
print ("I also said: '%s'." % y)

# define the variable 'hilarious' as the boolean value False
hilarious = False
# define the variable Isn't that joke so funny?!
joke_evaluation = "Isn't that joke so fuuny?! %r"

print (joke_evaluation % hilarious)

w = "This is the left side of..."
e = "a string with a right side"

print (w + e)
