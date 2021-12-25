#Write a Python program to count the number of strings where
# the string length is 2 or more and the first and last character
# are same from a given list of strings.

#Assigned Strings value to list named data
data = ["abcda", "1478", "1741", "awca", "fdk", "aa"]
#assigned total as 0
total = 0
#for loop to check in every item of list
for i in range(0, len(data)):
    #stored items of data in a step wise
    a = data[i]
    #check if length of string is greater than or equal to 2
    if len(a) >= 2:
        '''Assigned First Character of String to first and lst character
         of string to last respectively '''
        first = a[0]
        last = a[len(a) - 1]
        #check whether first and last character are same or not and add 1
        #each time as first and last characters are same.
        if first == last:
            total = total + 1

print(f"The Number of string having first and last character same and string length 2 is : {total}")
