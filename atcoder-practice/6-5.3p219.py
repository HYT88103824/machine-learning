N = int(input())

path = []
for i in  range(N):
    row = list(map(int,input().split()))
    path.append(row)

ALL = 1<<N

dist = []
for i in range(ALL+1):
    dist.append([float('inf')]*N)

dist[0][0] = 0

def check(n,j):
    return (n&1<<j > 0)


for n in range(ALL):  #
  for i in range(N):
      for j in range(N):
          if check(n,j) or i == j:
              continue
          dist[n|(1<<j)][j] = min(dist[n][i]+path[i][j],dist[n|(1<<j)][j])


print(dist[ALL-1][0])

