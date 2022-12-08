import os



with open('data.txt') as f:
    lines=f.read().splitlines()


#p1

count=0
for row in range(1,len(lines)-1):
    for col in range(1,len(lines[0])-1):

        if not ((any(int(x)>=int(lines[row][col]) for x in lines[row][0:col])) and (any(int(x)>=int(lines[row][col]) for x in lines[row][col+1:])) and (any(int(lines[x][col])>=int(lines[row][col]) for x in range(0,row))) and (any(int(lines[x][col])>=int(lines[row][col]) for x in range(row+1,len(lines))))):
            count+=1

        
print(count+4*len(lines)-4)

#p2

X=[]
for row in range(1,len(lines)):
    for col in range(0,len(lines[0])):
        
        x=[0,0,0,0]
        for i in range(row-1,-1,-1):
            x[0]+=1
            if not int(lines[row][col])>int(lines[i][col]):
                break

        for i in range(col-1,-1,-1):
            x[1]+=1
            if not int(lines[row][col])>int(lines[row][i]):
                break

        for i in range(row+1,len(lines)):
            x[2]+=1
            if not int(lines[row][col])>int(lines[i][col]):
                break

        for i in range(col+1,len(lines[0])):
            x[3]+=1
            if not int(lines[row][col])>int(lines[row][i]):
                break
        
        X.append(x[0]*x[1]*x[2]*x[3])

print(max(X))




