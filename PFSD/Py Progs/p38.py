n=int(input())
f=0
for i in range(2,int(n/2)+2):
    if n%i==0:
        f=1
        print("not a prime")
        break
else:print("it is a prime")
