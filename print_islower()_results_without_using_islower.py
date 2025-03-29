#Prog04. islower() check if all characters of the string is on lower case. Create a program that do the same functionality without using islower() function.
def low_taper_check(string):
    for char_checker in string:
        if char_checker.isupper():
            return False
    return True
#enter "help"
text = input("Enter a string: ")
#print "true"
print(low_taper_check(text))