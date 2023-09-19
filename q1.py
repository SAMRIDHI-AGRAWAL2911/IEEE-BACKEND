s1=input("enter the first string:")
s2=input("enter the second string:")
l1=len(s1)
l2=len(s2)
v=False
for i in range(0,l1):
    v=False
    for j in range(0,l2):
        if (s1[i]==s2[j]):
            v=True
            break
    if(v==False):
        print("the strings s1 & s2 are not balanced")
        break
if(v==True):
    print("the strings entered are balanced")