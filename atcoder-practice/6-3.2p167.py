import sys
sys.setrecursionlimit(1000000)

H,W = map(int,input().split())

town = []
visited = []
count = 0

for i in range(H):
    row = input()
    town.append(row)
    visited.append([False]*W)


for i in range(H):
    for j in range(W):
        if town[i][j] == 's' :
            start = [i,j]
        if town[i][j] == 'g' :
            goal = [i,j]


def dfs(i,j): 
    for u,v in [[i-1,j],[i+1,j],[i,j+1],[i,j-1]]:
        if 0<=u<H and 0<=v<W:
          if  town[u][v] == '.':
              if not visited[u][v]:
                visited[u][v] = True
                dfs(u,v)                
          if town[u][v] == 'g':
              visited[u][v] = True
              break

dfs(start[0],start[1])

if visited[goal[0]][goal[1]]:  #関数内で処理しようとせずvisitedを使う方がよい
    print('Yes')
else:
    print('No')
                