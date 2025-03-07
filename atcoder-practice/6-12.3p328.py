#キューを使う場合
#この場合はTLEとなってしまう
'''
from collections import deque

H,W = map(int,input().split())

mod = 10**9+7

maze = []
for i in range(H):
    row = input()
    maze.append(row)
    
visited = []
for i in range(H):
    visited.append([False]*W)

visited[0][0] = True  
count = 0

Q = deque()
Q.append((0,0))

while len(Q)>0:
  i,j = Q.popleft()
  visited[i][j] = True
  for i2,j2 in [(i+1,j),(i,j+1)]:
    if 0 <= i2 < H and 0 <= j2 < W and not visited[i2][j2]:
       if maze[i2][j2] == '.':
         Q.append((i2,j2))
       if i2 == H-1 and j2 == W-1:
         count += 1
         count = count%mod
         break

print(count)
'''
#右と下にしか動けないので動的計画法で解ける

H,W = map(int,input().split())

mod = 10**9+7

maze = []
for i in range(H):
    row = input()
    maze.append(row)
    
way = []
for i in range(H):
    way.append([0]*W)
    
way[0][0] = 1

for i in range(H):
  for j in range(W):
    if maze[i][j] == '#':
      continue
    if i > 0:
      way[i][j] += way[i-1][j]
    if j > 0:
      way[i][j] += way[i][j-1]
      
    way[i][j] %= mod
    
print(way[H-1][W-1])
  