#Prog06. rjust() add space characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using rjust() function.
text = "CAPTAIN!"
length = 12
#enter "CAPTAIN!"
text = "{:>12}".format(text)
#PRINT "    CAPTAIN!"
print(text)