import heapq

N,M = map(int,input().split())

route = []
for i in range(N):
    route.append([])
    
for i in range(M):
    u,v,c = map(int,input().split())
    route[u].append((v,c))             #できるだけ1つのリストに情報をまとめる

dist = []
visited = []
for i in range(N):  
    dist.append(-1) 
    visited.append(False) 
    
dist[0] = 0
Q = []
heapq.heappush(Q,(0,0))


while len(Q)>0:
    
    d,s = heapq.heappop(Q)
    
    if visited[s]:
        continue
    
    visited[s] = True
    
    for (x,y) in route[s]:
        if dist[x] == -1 or dist[x] > dist[s] + y:
            dist[x] = dist[s] + y
            heapq.heappush(Q,(dist[x],x))

print(dist[N-1])