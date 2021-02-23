"""
Given two strings, write a method to decide if one is a permutation of the
other.

"""
from collections import defaultdict

#sort
def isperm(s1,s2):
    if len(s1)!=len(s2):
        return False
    s1=sorted(s1)
    s2=sorted(s2)
    return s1==s2

#char count
def ispermutation(s1,s2):
    if len(s1)!=len(s2):
        return False

    d=defaultdict(int)
    for i in s1:
        d[i]+=1
    for i in s2:
        d[i]-=1
        if d[i]<0:
            return False
    return True

s1='dog'
s2='god'

print(isperm(s1,s2))
print(ispermutation(s1,s2))
         