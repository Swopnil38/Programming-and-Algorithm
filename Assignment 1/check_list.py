#Write a Python program to check a list is empty or not.
#empty list named num
num = []
#non-empty list named alpha
alpha = ["abcda","1478","1741","awca","fdk","aa"]
'''Check whether length of list is equal to 0 or not.
If Found 0 then the list is an empty list
and if not found 0 then it is not an empty list'''
if len(alpha) == 0:
    print(f"The List is an empty list.")
else:
    print(f"The list is not an empty list.")