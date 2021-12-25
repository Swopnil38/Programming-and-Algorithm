#Write a Python program to select an item randomly from a list.
#imported random
import random
#List named alpha
alpha = ["abcda","1478","1741","awca","fdk","aa","aq7u"]
#randomly take any numbers between 0 to length of list alpha and store to a
a = random.randint(0,len(alpha))
print(f"The Randomly selected item  is: {alpha[a]}")