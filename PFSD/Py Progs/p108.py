#prog to split and join a str
s="pfsd"
f=k=""

for i in range(len(s)):
    if i<2:
        f+=s[i]
    else:
        k+=s[i]
print(f,k)
j=f+k
print(j)