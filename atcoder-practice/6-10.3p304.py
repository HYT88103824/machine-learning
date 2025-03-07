N,M = map(int,input().split()) #2<=N<=100 なのでワーシャルフロイド法

route = []
for i in range(N):
    route.append([float('inf')]*N) #別のリストに距離を格納すると入力された経路の情報が反映できない

for i in range(M):
    u,v,c = map(int,input().split())
    route[u][v] = c

for i in range(N):   #同じ頂点間の距離は0
    route[i][i] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            route[i][j] = min(route[i][j],route[i][k]+route[k][j])
            
sum = 0
for i in range(N):
    for j in range(N):
        sum += route[i][j]
        
print(sum)