#Prog09. index() return the first location of the function parameter in the string. Create a program that do the same functionality without using index() function.
text = input("Enter a string: ")
goal = input("Enter what to find where and when it starts: ")
#EXAMPLE: "Purple"
index_bootleg = -1  

for index_occurence in range(len(text)):
    if text[index_occurence] == goal:
        index_bootleg = index_occurence
        break 

#print "2" (because "r" is at index 2)
print(index_bootleg)