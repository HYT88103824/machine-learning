import heapq

N,M = map(int,input().split())

route = []
for i in range(N):
    route.append([])

for i in range(M):
    u,v,c = map(int,input().split())
    route[u].append((v,c))
    route[v].append((u,c))

mark = []
for i in range(N):
    mark.append(False)
    
Q = []
heapq.heappush(Q,(0,0))
count = 0
sum = 0

while count < N:
    d,s = heapq.heappop(Q)
    
    if mark[s]:
        continue
    
    mark[s] = True
    count += 1
    sum += d

    for (x,y) in route[s]:
        if mark[x]:
             continue
        heapq.heappush(Q,(y,x))

print(sum)