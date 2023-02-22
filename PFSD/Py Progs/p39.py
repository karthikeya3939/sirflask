
c=0
for i in range(1,101):
    f=0
    
    for j in range(2,int(i/2)+2):
        if i%j==0:
            f=1
            break
    else:
        print(i)
        c+=1
print(c)
