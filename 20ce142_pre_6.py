'''NAME : khushi tala
   ID   : 20Ce142
'''
from collections import Counter    #import counter
n=int(input ())                    #take number of test cases from user
l=list()                           #list of string
for _ in range (n):
    l.append(input())              #add a string to existing string
x=Counter(l)                       #count the items in a iterable

print (len(x))
print(*x.values())                 #Unpacking a items using Asterisk operator
