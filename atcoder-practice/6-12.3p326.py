#再帰を利用した動的計画法
#この場合はTLEとなってしまう
'''
import sys
sys.setrecursionlimit(1000000)

N,M = map(int,input().split())

mod = 10**9 + 7

A = [False]*(N)
for i in range(M):
    a = int(input())
    A[a] = True

count = 0

def upstair(stair):
    if stair == N:
        global count
        count += 1
        count += count%mod
        return
    
    elif stair > N:
        return 
    
    if not A[stair]:
        upstair(stair+1)
        upstair(stair+2)
    else:
        return
        

upstair(0)
print(count)
'''
N,M = map(int,input().split())

mod = 10**9+7

A = [True]*(N+1)
for i in range(M):
    a = int(input())
    A[a] = False

cost = [0]*(N+1)
cost[0] = 1

for i in range(1,N+1):
    if A[i]:
        if i == 1:
            cost[i] = cost[i-1]
        else:
            cost[i] = (cost[i-1]+cost[i-2])%mod

print(cost[N]) 
        
