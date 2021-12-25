# Write a Python program to multiplies all the items in a list.
#imported math
import math
# created list named data
data = [1, 2, 3, 4, 5]
#product all item of data using prod operator of math and store in mult_total
mult_total = math.prod(data)
print(f"The multiplies of all item in a list: {data} is {mult_total}")
'''
#Assigned j as 1 as if j is 0 then the multiples will be 0
j = 1
#if else statement as if data is an empty list then the multiplies
#must be 0 rather than 1
if len(data)>=1:
    #for loop to multiplies every item in list and store in j
    for i in data:
        j = j * i
else:
    #j will bo 0 if data is an empty set
    j = 0
print(f"The multiplies of all item in a list: {data} is {j}")
'''
