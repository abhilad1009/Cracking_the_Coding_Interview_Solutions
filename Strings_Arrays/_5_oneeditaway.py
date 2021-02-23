"""
One Away: There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.
EXAMPLE
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bae -> false

"""

def oneeditaway(s1,s2):
    
    if abs(len(s1)-len(s2))>1:
        return False

    if len(s1)<len(s2):
        ss=s1
        sl=s2
    else:
        ss=s2
        sl=s1
    
    idx1=0
    idx2=0
    check=0

    while idx2<len(sl) and idx1<len(ss):
        if ss[idx1]!=sl[idx2]:
            if check:
                return False
            check=1

            if len(ss)==len(sl):
                idx1+=1
        else:
            idx1+=1
        idx2+=1
    
    return True

print(oneeditaway("pal","pale"))
print(oneeditaway("bal","pale"))
print(oneeditaway("bale","pale"))
    