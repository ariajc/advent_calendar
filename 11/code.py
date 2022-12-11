import os
import re
from math import prod 

os.chdir('C:\\Users\\AriaJaimejuan\\OneDrive - Mentice AB\\Desktop\\advent\\Nueva carpeta\\advent_calendar\\11')

with open('data.txt') as f:
    lines = f.read().split("\n\n")

class monkey:
    def __init__(self,items, operation,test,throw):
        self.items = items
        self.operation = lambda old: eval(operation)
        self.test=test
        self.throw=throw
        self.count=0

    def __len__(self): return len(self.items)

    def addItem(self,x): 
        self.items.append(x)
        #self.count+=1

    def delItem(self): 
        self.items.clear()

    
    def inspect(self):
        self.count+=len(self.items)
        

        


monkeys=[]
lines=[x.splitlines() for x in lines]
for element in lines:
    items=[int(x) for x in re.findall(r'\d+',element[1])]
    operation=element[2][19:]
    test=re.findall(r'\d+',element[3])
    throw=[re.findall(r'\d+',element[4]), re.findall(r'\d+',element[5])]

    monkeys.append(monkey(items,operation,test,throw))

#p1
for i in range(1,21):
    for element in monkeys:
        element.inspect()
        for x in element.items:
            new=element.operation(x)//3
            if new%int(element.test[0])==0:
                monkeys[int(element.throw[0][0])].addItem(new)
            else:
                monkeys[int(element.throw[1][0])].addItem(new)
        element.delItem()


X=[]
for element in monkeys:
    X.append(element.count)
X.sort()
print(X[-1]*X[-2])

#p2  

monkeys=[]

for element in lines:
    items=[int(x) for x in re.findall(r'\d+',element[1])]
    operation=element[2][19:]
    test=re.findall(r'\d+',element[3])
    throw=[re.findall(r'\d+',element[4]), re.findall(r'\d+',element[5])]

    monkeys.append(monkey(items,operation,test,throw))


mod = prod(int(m.test[0]) for m in monkeys)
for i in range(10000):
    for element in monkeys:
        element.inspect()
        for x in element.items:
            new=element.operation(x)%mod
            if new%int(element.test[0])==0:
                monkeys[int(element.throw[0][0])].addItem(new)
            else:
                monkeys[int(element.throw[1][0])].addItem(new)
        element.delItem()


X=[]
for element in monkeys:
    X.append(element.count)
X.sort()
print(X[-1]*X[-2])

