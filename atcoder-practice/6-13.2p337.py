import sys
sys.setrecursionlimit(1000000)

N = int(input())

sub = []
for i in range(N+1):
    sub.append([])
    
for i in range(1,N+1):
    p = int(input())
    if p == -1:
        continue
    else:
        sub[p].append(i) 
        
Q = int(input())
query = []
for i in range(Q):
    s,b = map(int,input().split())
    query.append([s,b])

check = []
for i in range(N+1):
    check.append([False]*(N+1))

def dfs(s,b,boss):
    if check[b][s]:
        return
    else:
        for x in sub[boss]:
           check[b][x] = True
           dfs(s,b,x)   
    return 

for s,b in query:
    boss = b
    dfs(s,b,boss)

for s,b in query:
    if check[b][s]:
        print('Yes')
    else:
        print('No')

