import os
import re




with open('data.txt') as f:
    lines=f.readlines()


## p1
sum=0
for f in lines:
    x=re.findall(r'\d+', f)
    y=set(range(int(x[0]),int(x[1])+1))
    z=set(range(int(x[2]),int(x[3])+1))
    if len(y.intersection(z))==len(y) or len(y.intersection(z))==len(z):
        sum+=1

print(sum)

##p2

sum_2=0
for f in lines:
    x=re.findall(r'\d+', f)
    y=set(range(int(x[0]),int(x[1])+1))
    z=set(range(int(x[2]),int(x[3])+1))
    if len(y.intersection(z))!=0:
        sum_2+=1

print(sum_2)