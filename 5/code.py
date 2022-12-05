import os
import re
import numpy as np






with open('data.txt') as f:
    lines_1,lines_2 = f.read().split("\n\n")

#P1
x=[]
for i in range(0,9):
    y=[]
    for line in lines_1.splitlines()[:-1]:
        string= line[(i* len(line)//9): ((i + 1)* len(line)//9)].strip()
        if string != "":
            y.append(string)
    x.append(y)
    

print(x)


for line in lines_2.splitlines():
    z=re.findall(r'\d+', line)
    x[int(z[2])-1]=list(reversed(x[int(z[1])-1][0:int(z[0])]))+x[int(z[2])-1]
    x[int(z[1])-1]=x[int(z[1])-1][int(z[0]):]
    
print(x)

#P2
x=[]
for i in range(0,9):
    y=[]
    for line in lines_1.splitlines()[:-1]:
        string= line[(i* len(line)//9): ((i + 1)* len(line)//9)].strip()
        if string != "":
            y.append(string)
    x.append(y)

for line in lines_2.splitlines():
    z=re.findall(r'\d+', line)
    x[int(z[2])-1]=x[int(z[1])-1][0:int(z[0])]+x[int(z[2])-1]
    x[int(z[1])-1]=x[int(z[1])-1][int(z[0]):]
    
print(x)


