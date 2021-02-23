"""
Given a string, write a function to check if it is a permutation of
a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A
permutation is a rearrangement of letters. The palindrome does not need to be limited to just
dictionary words.
EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat'; "atc o eta·; etc.)

"""
#O(n) time
#we consider only a-z for simplicity
from collections import defaultdict

def ispalinperm(s):
    oddct=False
    d=defaultdict(int)
    for i in s:
        d[s]+=1
    for j in d.values():
        if j%2==1:
            if oddct:
                return False
            oddct=True
    return True

s='tacocat'

print(ispalinperm(s))
