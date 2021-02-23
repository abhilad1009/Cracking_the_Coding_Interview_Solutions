"""
Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column are set to 0.
"""

def nullifyRow(M,row):
    for j in range(len(M[0])):
        M[row][j]=0

def nullifyCol(M,col):
    for i in range(len(M)):
        M[i][col]=0   

def setzeros(M):
    row1zero=False
    col1zero=False

    for j in range(len(M[0])):
        if M[0][j]==0:
            row1zero=True
            break

    for i in range(len(M)):
        if M[i][0]==0:
            col1zero=True
            break
    
    for i in range(1,len(M)):
        for j in range(1,len(M[0])):
            if M[i][j]==0:
                M[0][j]=0
                M[i][0]=0

    for i in range(1,len(M)):
        if M[i][0]==0:
            nullifyRow(M,i)

    for j in range(1,len(M[0])):
        if M[0][j]==0:
            nullifyCol(M,j)

    if row1zero:
        nullifyRow(M,0)
    if col1zero:
        nullifyCol(M,0)


M=[[1,2,0],[4,5,6],[7,8,9]]
for i in M:
    print(i)

setzeros(M)

for i in M:
    print(i)
