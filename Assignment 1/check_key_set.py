# Write a Python script to check if a given key already exists in a dictionary.
a = input("Enter a key to remove from Dictionary if it is present: ")
integer = {"first": 1, "third": 3, "fifth": 5, "second": 2, "ninty": 90}
#assigned b as 0
b = 0
#for loop to go in every key and values of dictionary
for key,value in integer.items():
    #if statement to check item of set is equal to user input
    if key == a:
        #if found then Show it exists as key
        print(f"{a} already exist as key in dictionary {integer}")
        break
    #else to count how many Key did not match user input
    else:
        b = b+1
#check if all key doesn't match
if b == len(integer):
    print(f"{a} is Not found in Dictionary : {integer}")




