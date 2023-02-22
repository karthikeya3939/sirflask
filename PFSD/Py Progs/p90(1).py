try:
    n=int(input())

except ValueError:
    print("exception")
    print(2/0)
except:
    print("error")
else:
    print("ur number is ",n)
finally:
    print("fuck of bitch")
    
