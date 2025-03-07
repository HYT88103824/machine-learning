import sys
sys.setrecursionlimit(1000000)

N,M = map(int,input().split())

path = []
for i in range(N):
    path.append([])
    
indeg = [0]*N
    

for i in range(M):
    x,y = list(map(int,input().split())) #入力により分類する
    path[x-1].append(y-1)
    indeg[y-1] += 1    #始点じゃなければ+1
    
length = [0]*N
done = [False]*N

def calculate(i):
    if done[i]:
        return length[i]
    length[i] = 0
    for j in path[i]:
        length[i] = max(length[i],calculate(j)+1)
    done[i] = True
    return length[i]

for i in range(N):
    if indeg[i] == 0:  #0なら始点
      calculate(i)

print(max(length))