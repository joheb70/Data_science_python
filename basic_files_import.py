#Objectives : import text file in Python
#Author : Abdul Joheb Ansari--------------------------------------------

myfile = open("fruits.txt")

file = (myfile.read())




#better way of importing files

with open("fruits.txt") as myfile:
    content = myfile.read()

print(content)

