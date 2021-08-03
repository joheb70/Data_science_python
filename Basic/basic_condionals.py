#Goal : Create a function to find mean from list and dict data types
#Author : Abdul Joheb Ansari ------------------------------

def mean(value):
    if isinstance(value,dict):
        mean_algorithm = sum(value.values())/len(value)
    else:    
        mean_algorithm = sum(value) / len(value)
    
    
    return mean_algorithm

monday_temparatures = [8.8, 9.1, 7.5]
student_grades = {"Priya": 9.1, "Sin": 8.8, "John": 7.5}
print(mean(monday_temparatures))

# fun with user input

user=(input("message :"))

print(f"{user.upper()} Abdul sahab")

def foo(names):
    return f"Hi {names}"
        







