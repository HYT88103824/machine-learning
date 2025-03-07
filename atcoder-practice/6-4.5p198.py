'''
N = int(input())
boss = []
for i in range(N-1):
    B = int(input())
    boss.append(B)

pay = []
for i in range(N):
    pay.append(0)

pay[N-1] = 1

sub = []
for i in range(N):
    sub.append([])

for i in range(1,N+1):
    for j in range(N-1):
      if i == boss[j]:
          sub[i-1].append(j+2)
    
for i in range(N-2,-1,-1):
    if len(sub[i]) >= 2:
      pay[i] = max(list(pay[x-1] for x in sub[i]))+min(list(pay[x-1] for x in sub[i]))+1
    if len(sub[i]) == 1:
        pay[i] = 2*pay[sub[i]-1]+1
    if len(sub[i])==0:
        pay[i] = 1

print(pay[0])
'''
'''
dfs
'''
#末端から根に向かうときは再帰のdfsが効果的

import sys
sys.setrecursionlimit(1000000)

N = int(input())

child = []
for i in range(N):
    child.append([])

for i in range(1,N): #部下を入力する形にする
    b = int(input())
    child[b-1].append(i)

def dfs(i):
    if len(child[i])==0:
        return 1
    else:
        values = []
        for j in  child[i]:
            values.append(dfs(j))
        return max(values)+min(values)+1
    
print(dfs(0))