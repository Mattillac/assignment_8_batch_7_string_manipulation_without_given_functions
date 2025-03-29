#Prog03. upper() converts all characters of the string into upper case. Create a program that do the same functionality without using upper() function.
def fixer_upper(text):
    upper_cut = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_cut = "abcdefghijklmnopqrstuvwxyz"
    final_cut = str.maketrans(lower_cut, upper_cut)
    return text.translate(final_cut)
# enter "darkness"
text = input("Enter a string: ")
#print "DARKNESS"
print(fixer_upper(text))
