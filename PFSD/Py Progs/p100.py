#to split array and add all elements and add all elements in 1st part
l=list(map(int,input().split()))
s=0
for i in range(0,int(len(l)/2)):
    s+=l[i]
print(s)