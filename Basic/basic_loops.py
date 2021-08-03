#Objectives : Learn About loops
#Author : Abdul Joheb Ansari----------------------------

monday_temparature = [9.1, 8.8, 7.6]

for temparature in monday_temparature:
    print(round(temparature))

for letter in "hello":
    print(letter.title())




#--------------------------------------

def celsius_to_kelvin(cels):
    return cels + 273.15

#That is a function that gets a number as input, adds 273.15 to it and returns the result. 
# A for loop allows us to execute that function over a list of numbers:

monday_temperatures = [9.1, 8.8, -270.15]
 
for temperature in monday_temperatures:
    print(celsius_to_kelvin(temperature))

# Objective : Looping through library
grocery_prices = {"Eggs" : 2.3, "Tortilla" : 2.8, "Tomatoes" : 4}

for prices in grocery_prices.keys():
    print(prices)

#----
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for key, value in phone_numbers.items():
     print("{} {}".format(key,value))

for value in phone_numbers.values():  #going to subsection of dictionary and manipulating values
    print(value.replace("+","00"))
