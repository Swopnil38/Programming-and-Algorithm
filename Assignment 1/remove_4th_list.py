# Write a Python program to print a specified list after removing the 4th elements
#list named alpha
alpha = ["abcda", "1478", "1741", "awca", "fdk", "aa", "aq7u"]
#empty list named alpha_new to store all data of alpha except 4th element
alpha_new = []
#for loop to run as much as length of alpha
for i in range(len(alpha)):
    #If the element is 4th then skip else append the element of alpha to alpha_new
    if i == 4:
        continue
    else:
        alpha_new.append(alpha[i])
print(alpha_new)
