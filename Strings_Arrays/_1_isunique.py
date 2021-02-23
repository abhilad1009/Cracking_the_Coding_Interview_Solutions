"""
Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures ?

"""
#O(n) time / O(1) space
def isunique(s):
    d={}
    for i in s:
        if d.get(i)==None:
            d[i]=1
        else:
            return False
    return True

#For a-z only
def isuniqueaz(s):
    chk=0
    for i in s:
        val=ord(i)-ord('a')
        if (chk & (1<<val))>0:
            return False
        chk = chk | (1<<val)
    return True

s='abnkA'
print(isunique(s))
s='abkda'
print(isuniqueaz(s))

"""
If we can't use additional data structures, we can do the following:
1. Compare every character of the string to every other character of the string. This will take 0( n2) time
and 0(1) space.
2. If we are allowed to modify the input string, we could sort the string in O(n log(n)) time and then
linearly check the string for neighboring characters that are identical. Careful, though: many sorting
algorithms take up extra space.

"""