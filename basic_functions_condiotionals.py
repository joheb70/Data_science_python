#Goal : Create a function to find mean from list and dict data types
#Author : Abdul Joheb Ansari ------------------------------

def mean(value):
    if type(value) == dict:
        mean_algorithm = sum(value.values())/len(value)
    else:    
        mean_algorithm = sum(value) / len(value)
    
    
    return mean_algorithm

monday_temparatures = [8.8, 9.1, 7.5]
student_grades = {"Priya": 9.1, "Sin": 8.8, "John": 7.5}
print(mean(monday_temparatures))


