N = int(input())
p = list(map(int,input().split()))
p.insert(0,0)
M = sum(p)
l = []
for i in range(N+1):
    row = [False]*(M+1)
    l.append(row)
    
l[0][0] = True

for i in range(1,N+1):
    for j in range(M+1):
        if l[i-1][j]:
            l[i][j] = True
        if j-p[i] >= 0 and l[i-1][j-p[i]]:
            l[i][j] = True

count = 0
        
for x in l[N]:
    if x:
        count += 1

print(count)