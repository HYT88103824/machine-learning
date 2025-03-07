N,M = map(int,input().split())
R = []

for i in range(N):
    A = input()
    R.append(A)
    
group = []
for i in range(11):
    group.append([])
    
for i in range(N):
    for j in range(M):
        if R[i][j] == 'S':              #if,elif.elseをきちんと書く
            group[0].append([i,j])
        elif R[i][j] == 'G':
            group[10].append([i,j])
        else:
            n = int(R[i][j])
            group[n].append([i,j])

cost = []            
for i in range(N):
    cost.append([float('inf')]*M)
    
si,sj = group[0][0]
cost[si][sj] = 0

for n in range(1,11):
    for i,j in group[n]:
        for i2,j2 in group[n-1]:
          cost[i][j] = min(cost[i][j],cost[i2][j2] + abs(i-i2) + abs(j-j2))
                                                      #マンハッタン距離

#経路に1,2,3．．．9をこの順に'含む'ことが必要で1->2->3・・・->Gとなる必要はない
#①->5->4->②->7->③　のような経路も可能
gi,gj = group[10][0]
ans = cost[gi][gj]
if ans == float('inf'):
    print(-1)
else:
    print(ans)