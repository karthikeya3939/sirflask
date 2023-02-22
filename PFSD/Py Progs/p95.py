#Armstrong number
n=input()
s=0
x=len(n)
for i in n:
    s+=int(i)**x
if int(n)==s:
    print("armstrong")
else:
    print("no")