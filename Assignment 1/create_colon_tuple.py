#Write a Python program to create the colon of a tuple.
#imported deepcopy
from copy import deepcopy
#tuple named tup
tup = (7,8,4,5,11,78,47,55,122,178,999,456,985)
print(f"Orginal Tuple : {tup}")
#Copied all items of tup to tup_copy
tup_copy = deepcopy(tup)
print(f"Colon of Tuple: {tup_copy}")