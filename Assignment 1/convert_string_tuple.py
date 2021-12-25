#Write a Python program to convert a tuple to a string.
#created tuple named tup
tup = ('s','w','o','p','n','i','l')
# using for loop
'''
#Here every items of tuples keeps on adding to stri string 
#later forming a string
stri = ""
for items in tup:
    stri = stri + items
'''
#using str.join
#.join allows to add items of Tuples to a empty string converting its
#data type to string.
stri = "".join(tup)
print (stri)
print(type(stri))