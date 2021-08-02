#Learn while loop with user input
#Author : Abdul Joheb Ansari


username = ''

#while username != 'pypy':
    #username = input("Enter username:")

#second example 
while True:
    username = input("Enter Username Please:")
    if username == 'pypy':
        break
    else:
        continue



#third example of while loop

i=0

while i<10000:
    i = i + 1
    print(i)
 
    