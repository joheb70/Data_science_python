# Second Python file for basic on basic of Python
#Author : Abdul Joheb Ansari---------------------------------------------------------------------------


practice_list = [1 , 7, 9 ,7]

#append and extend method within list
practice_list.append(98)
practice_list.extend((7,9,9))
practice_list.extend(range(1,10))

print(practice_list)

#Index method
x= practice_list.index(8)
print(x)

#using append to consolidate two lists

workdays = ["Mon", "Tue", "Wed", "Thu", "Fri"]
weekend = ["Sat", "Sun"]
workdays.append(weekend[1])
print(workdays)
 # -1 index refers to the last item in the list idea of positive and negative index
print(workdays[-1])    
# splice and finding out last two items with negative indexing
print(workdays[-2:]) 



