N = int(input())
H = list(map(int,input().split()))

cost = [0]*N
cost[0] = 0

cost[1] = cost[0] + abs(H[0]-H[1])
 
for i in range(2,N):
    cost[i] = min(cost[i-1] + abs(H[i-1]-H[i]),cost[i-2]+abs(H[i-2]-H[i]))

print(cost[N-1])