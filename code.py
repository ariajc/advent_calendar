import os
import collections


os.chdir('C:/Users/AriaJaimejuan/OneDrive - Mentice AB/Desktop/advent/2/')



with open('data.txt') as f:
    matrix = [list(line.strip()) for line in f]

for row in matrix:
    del row[1]




def win(X):
    if ((X[1]=='X' and X[0]=='A')or(row[1]=='Y' and X[0]=='B')or(X[1]=='Z' and X[0]=='C')):
        ans=3
    elif((X[1]=='X' and X[0]!='B')or(X[1]=='Y' and X[0]!='C')or(X[1]=='Z' and X[0]!='A')):
        ans=6
    else:
        ans=0

    return ans

sum=0
sum_2=0
for row in matrix:
    sum=sum+win(row)
    if row[1]=='X':
        sum_2=sum_2+1
    elif row[1]=='Y':
        sum_2=sum_2+2
    elif row[1]=='Z':
        sum_2=sum_2+3


    
print(sum)
print(sum_2)
print(sum+sum_2)


sum=0
for row in matrix:
    if row[1]=='X':
        if row[0]=='A':
            sum=sum+3
        elif row[0]=='B':
            sum=sum+1
        else:
            sum=sum+2
    elif row[1]=='Y':
        sum=sum+3
        if row[0]=='A':
            sum=sum+1
        elif row[0]=='B':
            sum=sum+2
        else:
            sum=sum+3
    elif row[1]=='Z':
        sum=sum+6
        if row[0]=='A':
            sum=sum+2
        elif row[0]=='B':
            sum=sum+3
        else:
            sum=sum+1

print(sum)