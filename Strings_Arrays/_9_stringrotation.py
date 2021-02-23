"""
String Rotation: Assume you have a method i 5Su b 5 tr ing which checks if one word is a substring
of another. Given two strings, 51 and 52, write code to check if 52 is a rotation of 51 using only one
call to i5Sub5tring (e.g., "waterbottle" is a rotation of" erbottlewat").

"""

def isrotation(s1,s2):

    if len(s1)==len(s2) and len(s1)>0:

        s1s1=s1+s1

        if s1s1.find(s2)!=-1:
            return True
    
    return False

s1='waterbottle'
s2='erbottlewat'

print(isrotation(s1,s2))