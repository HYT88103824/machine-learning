N,K = map(int,input().split())
H = list(map(int,input().split()))

cost = [0]*N 
cost[0] = 0
cost[1] = cost[0] + abs(H[0]-H[1])

for i in range(2,N):
    cost[i] = min([cost[i-j] + abs(H[i-j]-H[i]) for j in range(1,K+1) if i-j >=0])
              
print(cost[N-1])

