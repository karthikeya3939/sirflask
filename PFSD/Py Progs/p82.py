import csv
import os
os.chdir("..")
with open("Book1.csv",mode="r")as file:
    c=csv.reader(file)
    print(c)
    for i in c:
        print(type(i))
        if len(i)!=0:
            print(i)
