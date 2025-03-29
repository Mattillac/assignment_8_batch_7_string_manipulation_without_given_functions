#Prog02. removesuffix() remove the characters at the end of the string that matches the function parameter. Create a program that do the same functionality without using removesuffix() function.
text = "doom.exe"
suffix = ".exe"
#example "doom.exe"
if text.endswith(suffix):
        text = text[:-len(suffix)]
#print "doom"
print(text)