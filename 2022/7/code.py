import os
import re



with open('data.txt') as f:
    lines=f.readlines()

##p1
sum=0
X=[]
for line in lines:
    if '..' in line:
        if X[0]<100000:
            sum+=X[0]
        X.pop(0)
    elif '$ cd' in line: 
        X.insert(0,0)
    elif len(re.findall(r'\d+', line))!=0:
        X=[x+int(re.findall(r'\d+', line)[0]) for x in X]
        
 
print(sum)

##p2

tot=0
for line in lines:
    if len(re.findall(r'\d+', line))!=0:
        tot+=int(re.findall(r'\d+', line)[0])


X=[]
directories=[]
for line in lines:
    if '..' in line:
        if X[0]>=30000000-(70000000-tot):
            directories.append(X[0])
        X.pop(0)
    elif '$ cd' in line: 
        X.insert(0,0)
    elif len(re.findall(r'\d+', line))!=0:
        X=[x+int(re.findall(r'\d+', line)[0]) for x in X]

print(min(directories))