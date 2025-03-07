'''
num = list(map(int,input().split())) #N M Q
lines = []
queri = []
color = []

for i in range(num[1]):
    line = []
    line = list(map(int,input().split()))
    lines.append(line) 
    

color = list(map(int,input().split()))

for i in range(num[2]):
  q = list(map(int,input().split()))
  query.append(q)


def spring(q):
    if len(q) == 2:
        print(color[q[1]-1])
        for x in lines:
            if x[0] == q[1]:
                color[x[1]-1] = color[x[0]-1]
            if x[1] == q[1]:
                color[x[0]-1] = color[x[1]-1]
    if len(q) == 3:
        print(color[q[1]-1])
        color[q[1]-1] = q[2]


for x in query:
    spring(x)
'''
'''
隣接行列
''' 
'''
N,M,Q = map(int,input().split())

gragh = []
for i in range(N):
    row = []
    for j in range(N):
        row.append(False)
    gragh.append(row)

for i in range(M):
    u,v = map(int,input().split())
    u -= 1
    v -= 1
    gragh[u][v] = True
    gragh[v][u] = True

C = list(map(int,input().split()))
Query = []

for i in range(0,Q):
    q = []
    q = list(map(int,input().split()))
    Query.append(q)
    
for query in Query:
  if query[0] == 1:
      x = query[1]
      x -=1
      print(C[x])
      
      for i in range(N):
          if gragh[x][i]:
              C[i]=C[x]
  if query[0]==2:
      x = query[1]
      y = query[2]
      x-=1
      print(C[x])
      C[x] = y
'''
'''
隣接リスト
'''
N,M,Q = map(int,input().split())
gragh = []

for i in range(N):
   line= []
   gragh.append(line)

for i in range(M):  
  u,v = map(int,input().split())
  u -= 1
  v -= 1
  gragh[u].append(v)
  gragh[v].append(u)

C = list(map(int,input().split()))

Query = []
for i in range(0,Q):
    q = []
    q = list(map(int,input().split()))
    Query.append(q)
    
    
for query in Query:
  if query[0] == 1:
      x = query[1]
      x -=1
      print(C[x])
      for i in gragh[x]:
        C[i]=C[x]
        
  if query[0]==2:
      x = query[1]
      y = query[2]
      x-=1
      print(C[x])
      C[x] = y


                  
                  
          
    