import os



with open('data.txt') as f:
    lines=f.readlines()


#p1
X=[]
y=0
x=1
for line in lines:
    if len(line.split())>1:
        _,num=line.split()
        X+=[x]*2
        y+=2
        x+=int(num)
    else:
        X.append(x)
        y+=1

cycle=list(range(1,y+1))   
   
print(sum([X[int(i-1)]*cycle[int(i-1)] for i in list(range(20,((241-20)//40+1)*40,40))]))

#p2
CPR=[]
count=0

for element in X:
    print(count)
    print(list(range(int(element)-1,int(element)+2)))
    if count in list(range(int(element)-1,int(element)+2)):
        CPR.append('#')
    else:
        CPR.append('.')

    if count == 39:
        count = 0
    else:
        count+=1

CPR=''.join(CPR)

print(CPR[0:40])
print(CPR[41:80])
print(CPR[81:120])
print(CPR[121:160])
print(CPR[161:200])
print(CPR[201:240])