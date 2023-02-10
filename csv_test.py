import csv

f=open(r"e:\py\a.csv", 'r', encoding='utf8')
#print(f.read())

new=csv.reader(f)
data=[row for row in new]

for i in data:
    print(i)

print(data[0])