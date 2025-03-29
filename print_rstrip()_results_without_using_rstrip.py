#Prog01. rstrip() remove the space characters at the end of the string. Create a program that do the same functionality without using rstrip() function.
text = input("Enter a string: ")
#enter "FOR DEMACIA!   "
while text.endswith(" "):
    text = text[:-1]
#print "FOR DEMACIA!"
print(text)