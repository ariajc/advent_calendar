import os


os.chdir('C:\\Users\\AriaJaimejuan\\OneDrive - Mentice AB\\Desktop\\advent\\Nueva carpeta\\advent_calendar\\9')

with open('data.txt') as f:
    lines=f.read().splitlines()

vals = {'R':1,'L':-1,'U':1,'D':-1}


#p1
vect_tail=[0,0]
pos_head=[]
pos_tail=[]
pos_head.append([0,0])
pos_tail.append([0,0])
for line in lines:
    dir,step  = line.split()
    for i in range(0,int(step)):
        if dir=='U' or dir=='D':
            x=pos_head[-1][0]+vals[dir]
            y=pos_head[-1][1]
        else:
            x=pos_head[-1][0]
            y=pos_head[-1][1]+vals[dir]
        pos_head.append([x,y])
        

        if (pos_head[-1][0]-vect_tail[0])**2+(pos_head[-1][1]-vect_tail[1])**2>2:
           vect_tail= pos_head[-2]
           pos_tail.append(vect_tail)



pos_tail = [i for n, i in enumerate(pos_tail) if i not in pos_tail[:n]]
#print(pos_tail)
print(len(pos_tail))

#p2
moves=[[0,1],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1],[-1,0],[1,0]]

def min_move(B,A):
    moves_AB=[(B[0]-(A[0]+i[0]))**2+(B[1]-(A[1]+i[1]))**2 for _, i in enumerate(moves)]
    return moves[moves_AB.index(min(moves_AB))]

knots=[[0,0] for i in range(10)]

pos_tail=[]
for line in lines:
    dir,step  = line.split()
    for i in range(0,int(step)):
        if dir=='U' or dir=='D':
            knots[0][0]+=vals[dir]
        else:
            knots[0][1]+=vals[dir]

        for j in range(0,len(knots)-1):
            if (knots[j][0]-knots[j+1][0])**2+(knots[j][1]-knots[j+1][1])**2>2:
                knots[j+1]=[knots[j+1][0]+min_move(knots[j],knots[j+1])[0],knots[j+1][1]+min_move(knots[j],knots[j+1])[1]]
        
        pos_tail.append(knots[9])


pos_tail = [i for n, i in enumerate(pos_tail) if i not in pos_tail[:n]]
#print(pos_tail)
print(len(pos_tail))


    