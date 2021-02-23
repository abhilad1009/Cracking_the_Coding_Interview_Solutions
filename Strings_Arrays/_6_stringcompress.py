"""
String Compression: Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).

"""

def compress(s):
    L=[]
    ct=0

    for i in range(len(s)):
        ct+=1

        if i+1>=len(s) or s[i]!=s[i+1]:
            L.append(s[i])
            L.append(ct)
            ct=0
        
    cs="".join(str(i) for i in L)
    if len(cs)>len(s):
        return s
    else:
        return cs

s1="aabcccccaaa"
s2="abc"

print(compress(s1))
print(compress(s2))

