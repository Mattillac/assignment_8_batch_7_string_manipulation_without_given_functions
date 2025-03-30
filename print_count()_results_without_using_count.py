#Prog08. count() return how many time the function parameter appear in the string. Create a program that do the same functionality without using count() function.
from collections import Counter
#read "Mushroooms!"
text = input("Enter a random word or number: ")
your_target = input("Enter the character to count: ")
counter_texterists = Counter(text)
#print "there are 3 os in "Mushroooms!"
print(counter_texterists[your_target])