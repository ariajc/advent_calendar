import os



with open('data.txt') as f:
    lines=f.read()

##p1
for i in range(0,len(lines)):
    if len(set(lines[i:(i+4)]))==4:
        print(i+4)
        break

##p2
for i in range(0,len(lines)):
    if len(set(lines[i:(i+14)]))==14:
        print(i+14)
        break