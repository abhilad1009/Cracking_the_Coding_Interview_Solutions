"""
Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
"""
import math

def rotate(M):
    if len(M)==0 or len(M)!=len(M[0]):
        return False
    
    for layer in range(math.ceil(len(M)/2)):
        first=layer
        last=len(M)-first-1

        for i in range(first,last):
            offset=i-first
            top=M[first][i]
            M[first][i]=M[last-offset][first]
            M[last-offset][first]=M[last][last-offset]
            M[last][last-offset]=M[i][last]
            M[i][last]=top
    
    return True

M=[[1,2,3],[4,5,6],[7,8,9]]

for i in M:
    print(i)

rotate(M)

for i in M:
    print(i)