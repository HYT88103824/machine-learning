from collections import deque

N = int(input())

A = list(map(int,input().split()))

B = deque()

#2**NはO(N)なので注意
for x in A:
    B.append(x)
    while len(B) > 1:
      if B[-1] != B[-2]:
          break
      elif B[-1] == B[-2]:
          sum = B[-1]+1
          B.pop()
          B.pop()
          B.append(sum)
      
print(len(B))

