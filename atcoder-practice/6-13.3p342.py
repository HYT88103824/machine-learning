from collections import deque

N = int(input())
Q = int(input())

dque = deque()

def matrix(que,i,j):
  while len(que) > 0:
    x = que.pop()
      
    if x[0] == 1:
        if i == x[1]:
            i = x[2]
        elif i == x[2]:
            i = x[1]
                   
    elif x[0] == 2:
        if j == x[1]:
            j = x[2]
        elif j == x[2]:
            j = x[1]
            
    elif x[0] == 3:
        s = i
        i = j
        j = s
  return (i,j)
        
ans = []
query = []
for i in range(Q):
    q = list(map(int,input().split()))
    if q[0] == 4:
        i,j =matrix(dque,q[1],q[2])
        ans.append(N*(i-1)+j-1)
        dque = deque(query)
    else:
      query.append(q)
      dque.append(q)
    
for x in ans:
    print(x)