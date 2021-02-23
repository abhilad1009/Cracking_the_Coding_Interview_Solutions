"""
Write a method to replace all spaces in a string with '%20'. You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string. (Note: if implementing in Java, please use a character array so that you can
perform this operation in place.)
EXAMPLE
Input: "Mr John Smith ", 13
Output: "Mr%20John%20Smith"

"""
#s is  a list. Strings are immutable. S has buffer space at end. Length of s is given.
def url(s,l):
    ct=0
    for i in range(l):
        if s[i]==' ':
            ct+=1
    idx=l+ct*2
    for i in range(l-1,-1,-1):
        if s[i]==' ':
            s[idx-1]='0'
            s[idx-2]='2'
            s[idx-3]='%'
            idx-=3
        else:
            s[idx-1]=s[i]
            idx-=1
    
s= list("Mr John Smith    ")
url(s,13)
print(s)

