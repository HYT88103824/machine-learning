from collections import deque

N,M = map(int,input().split())

path = []
for i in range(N):
    path.append([])
    
for i in range(M):
    u,v = map(int,input().split())
    path[u-1].append(v-1)
    path[v-1].append(u-1)

s = int(input())
s -= 1
K = int(input())

T = list(map(int,input().split()))
for i in range(K):
    T[i] -= 1

T.append(s)

Dist = []
for t1 in T:
    INF = 10**100
    dist = [INF]*N
    Q = deque()
    Q.append(t1)
    dist[t1] = 0
    while len(Q) > 0:
        i = Q.popleft()
        
        for j in path[i]:
            if dist[j] == INF:
                dist[j] = dist[i]+1
                Q.append(j)
    res = []
    for t2 in T:
        res.append(dist[t2])
    Dist.append(res)
 

ALL = 1<<K
cost = []
for i in range(ALL):
    cost.append([INF]*K)

for i in range(K):
    cost[1<<i][i] = Dist[K][i] #index Kはstartを表す


for n in range(ALL):
    for a in range(K):
        for b in range(K):
            if n&(1<<b) > 0 or a == b:
                continue
            cost[n|(1<<b)][b] = min(cost[n|(1<<b)][b],cost[n][a]+Dist[a][b])
            
print(min(cost[ALL-1]))