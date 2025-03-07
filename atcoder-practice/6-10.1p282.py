from collections import deque
import heapq

N,M = map(int,input().split())

route = []
for i in range(N+1):
    route.append([])

for i in range(M):
    a,b = map(int,input().split())
    route[a].append(b)
    route[b].append(a)


Q = deque()
Q.append(1)
visited = [True]+[False]*N
cost = [0]*(N+1)

while len(Q)>0:
    p = Q.popleft()
 
    for q in route[p]:
      if not visited[q]:
        visited[q] = True
        Q.append(q)
        cost[q] = cost[p]+1

if visited[N] and cost[N] == 2:
    print('POSSIBLE')
else:
    print('IMPPOSIBLE')

 
dist = []
for i in range(N+1):
    dist.append(-1)
    
done = []
for i in range(N+1):
    done.append(False)

Q = []
heapq.heappush(Q,(0,1)) #距離,頂点 距離でヒープする

dist[0] = 0
dist[1] = 0

while len(Q)>0:
    d,i = heapq.heappop(Q)
    
    if done[i]:
        continue
    
    done[i] = True
    
    for j in route[i]:
        x = 1
        
        if dist[j] == -1 or dist[j]>dist[i]+x:
            dist[j] = dist[i] + x
            heapq.heappush(Q,(dist[j],j))

if dist[N] == 2:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')