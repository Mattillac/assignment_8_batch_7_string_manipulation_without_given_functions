#Prog10. rindex() return the first location of the function parameter in the string starting from the last character. Create a program that do the same functionality without using rindex() function.
#EXAMPLE "Green"
text = input("Enter a word: ")
goal = input("Enter what to find where and when it starts: ")
index_bootleg = -1  

for index_occurence in range(len(text) - 1, -1, -1):  
    if text[index_occurence:index_occurence + len(goal)] == goal:
        index_bootleg = index_occurence
        break  

print(index_bootleg)
#print "the last E is at index 3"