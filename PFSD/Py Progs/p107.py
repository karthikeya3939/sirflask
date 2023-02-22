#to check whether the given string contains any spl char or not 97122 65 90
s=input()
for i in s:
    x=ord(i)
    if (x>=65 and x<=90) or(x>=97 and x<=122):
        continue
    else:
        print("NO")
        break
else:
    print("Yes")