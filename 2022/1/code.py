import os
import operator



with open('data.txt') as f:
    lines=f.readlines()



x=[]
sum=0

for i in range(0,len(lines)):
    if lines[i].strip():
        sum=sum+int(lines[i])
    else:
        x.append(sum)
        sum=0
        

max_value = max(x)
max_index = x.index(max_value)

indexed = list(enumerate(x))
top_3 = sorted(indexed, key=operator.itemgetter(1))[-3:]
list(reversed([i for i, v in top_3]))
print(max_value)
print(max_index)
print(list(reversed([i for i, v in top_3])))

print(x[151]+x[191]+x[99])
