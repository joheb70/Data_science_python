
#The start of Python Mega Course
#Author: Abdul Joheb Ansari------------------------------------------------------------------------------------------------------

# 1st program : Learn basic of modular code 
day_hours = 24
week_days = 7

week_hours = day_hours * week_days

print(week_hours)



# 2nd program : Learn about integer,string, and float data type
x =  10     
y = "10"     
z = 10.10   


sum_a = x + x    # Results in  -> 20
sum_b = y + y    # concatanate to -> 1010

print(sum_a, sum_b)
print(type(x), type(y), type(z))   #function to find data type of the object stored in the variables



# 3rd program : Learn about list data type
student_grades = [9.1, 8.8, 7.5]  #exampe of list data type
student_grades = {"Ram" : 9.1, "Shyam": 8.8, "Guam": 7.5}

grade_sum = sum(student_grades)
length = len(student_grades)
mean = grade_sum / length
print(mean)


#list can be created using range function
print(list(range(1, 5)))

#understanding attributes

print("hello".upper())   #use dir(data_type) in shell to find atrributes relating that data type
# use help(str.upper) for example for documentation about attributes


