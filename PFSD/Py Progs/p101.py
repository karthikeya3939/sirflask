#program to interchange 1st and last element of a list
l=list(map(int,input().split()))
l[0],l[-1]=l[-1],l[0]
print(l)