#prog to print even len words in a given string(sentens)
s=input()
l=s.split(" ")
c=0
for i in l:
    if len(i)%2==0:
        c+=1
print(c)