from collections import deque

R,C = map(int,input().split())
start = list(map(int,input().split()))
goal = list(map(int,input().split()))
maze = []
visited = []

start[0] -= 1
start[1] -= 1
goal[0] -= 1
goal[1] -= 1

for i in range(R):
    row = input()
    maze.append(row)

for x in range(R):
    visited.append([-1]*C)
            
Q = deque()
Q.append(start)
visited[start[0]][start[1]] = 0


while len(Q) > 0:
    i,j = Q.popleft()
    for i2,j2 in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]: ##4方向の処理は覚える
        if not (0<=i2<C and 0<=j2<R):
            continue
        if maze[i][j] == '#':
            continue
        if visited[i2][j2] == -1:
          visited[i2][j2] = visited[i][j]+1
          Q.append([i2,j2])
        
        
print(visited[goal[0]][goal[1]])    
         

            