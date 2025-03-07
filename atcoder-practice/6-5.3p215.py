#集合×動的計画法の問題

'''
N,M = map(int,input().split())

data = []
for i in range(M):
    row = list(map(str,input().split()))
    row[1] = int(row[1])
    data.append(row)

group = []

for x in data:
    YN = set()
    for y in x[0]:
        if y == 'Y':
            YN.add(1)
        if y == 'N':
            YN.add(0)
    group.append(YN)
            
cost = data[0][1]

for i in range(1,M):
    if group[i-1] - group[i] != {0*i for i in range(N)}:
        cost += data[i][1]
    group[i] = group[i-1]|group[i]
    #setは各要素ごとに和集合積集合をとるわけではない

check = {0*i for i in range(N)}
same = check&group[M-1]

if same == 0:
    print(cost)
else:
    print(-1)
'''
N,M = map(int,input().split())

S = [0]
C = [0]

for i in range(M):
    s,c =  input().split()
    s_val = 0
    for j in range(N):
        if s[j] == 'Y':
            s_val |= 1<<j
    S.append(s_val)
    C.append(int(c))

ALL = 1<<N

cost = []
for i in range(M+1):
    cost.append([float('inf')]*ALL)
    
cost[0][0] = 0

for i in range(1,M+1):  #全てのセットについて購入の判断をするときに部品の集合すべてを考える
    for j in range(ALL):
        
        cost[i][j] = min(cost[i][j],cost[i-1][j])
        
        cost[i][j|S[i]] = min(cost[i][j|S[i]],cost[i-1][j]+C[i])

ans = cost[M][ALL-1]  # ALL-1 = 1111111・・・11111111

if ans == float('inf'):
    ans = -1

print(ans)