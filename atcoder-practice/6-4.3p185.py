N,W = map(int,input().split())
ws = [0]
vs = [0]

for i in range(N):
  w,v = list(map(int,input().split()))
  ws.append(w)
  vs.append(v)

value = []
for i in range(N+1):
    value.append([-10**18]*(W+1))
    
value[0][0] = 0


for i in range(1,N+1):
  for w in range(W+1):
      value[i][w] = max(value[i][w],value[i-1][w])
      
      if w-ws[i] >= 0:
          value[i][w] = max(value[i][w],value[i-1][w-ws[i]]+vs[i])


print(max(value[N]))