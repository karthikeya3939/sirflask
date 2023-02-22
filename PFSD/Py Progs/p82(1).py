import csv

with open("Book1.csv","r")as m:
    c=csv.reader(m)
    for i in c:
        print(i)
