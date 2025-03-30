#Prog07. zfill() add zero characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using zfill() function.
#enter "123"
text = int(input("Enter 3 numbers: "))
length = int(input("Enter the length of the string: "))
text = f"{text:0>{length}}"
#print "000123"
print(text)