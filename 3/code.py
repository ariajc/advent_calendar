import string
import os


os.chdir('C:/Users/AriaJaimejuan/OneDrive - Mentice AB/Desktop/advent/3/')

values = dict()
for index , letter in enumerate(string.ascii_lowercase+string.ascii_uppercase):
    values[letter]=index+1

with open('data.txt') as f:
    lines=f.readlines()

sum=0

for line in lines:
    s_1=line[slice(len(line)//2)]
    s_2=line[slice(len(line)//2,len(line))]
    sum+=values[list(set(s_1).intersection(set(s_2)))[0]]
            
print(sum)


# ## p2
sum_2=0
for i in range(0,len(lines),3):
    x=lines[i]+lines[i+1]+lines[i+2]
    y=list(set(lines[i].strip()))+list(set(lines[i+1].strip()))+list(set(lines[i+2].strip()))
    print(x)
    for i in y:
        if y.count(i)==3:
            sum_2+=values[i]/3

print(sum_2)


