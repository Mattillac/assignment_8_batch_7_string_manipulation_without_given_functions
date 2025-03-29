#Prog05. startswith() check if the string beginning part matches the function parameter. Create a program that do the same functionality without using startswith() 
text = input("Enter a word: ")
start_checker = input("Enter the word to check: ")
#enter "FOR DEMACIA"
if text.find(start_checker) == 0:
    print(True)
#print true