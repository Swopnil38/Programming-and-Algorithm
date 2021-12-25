# Write a Python program to remove an item from a set if it is present in the set.
#Set named Integer
integer = {1, 2, 3, 4, 5, 6}
#taken a Number to remove from set
a = int(input("Enter a number to remove from set if it is present: "))
#assigned b as 0
b = 0
#for loop to go in every item of set
for item in integer:
    #if statement to check item of set is equal to user input
    if item == a:
        #if found then remove item from set integer
        integer.remove(a)
        print(f"The Modified set after removing {a} is : {integer}")
        break
    #else to count how many item did not match user input
    else:
        b = b+1
#check if all item doesn't match
if b == len(integer):
    print(f"{a} is Not found in Set : {integer}")