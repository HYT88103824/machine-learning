N,L = map(int,input().split())
X = list(map(int,input().split()))
T1,T2,T3 = map(int,input().split())

cost = [0]*(L+1)
h = [-1]*(L+1)
for i in range(N):
  h[X[i]] = X[i]

'''
for i in range(L+1):
    if i == h[i]:
      if 4 <= i:
        cost[i] = T3 + min(cost[i-1]+T1,cost[i-2]+T1+T2,cost[i-4]+T1+T2*3)
      elif 2 <= i:
        cost[i] = T3 + min(cost[i-1]+T1,cost[i-2]+T1+T2)
      elif i == 1:
        cost[i] = T3 + T1  
    else:
      if 4 <= i:
        cost[i] = min(cost[i-1]+T1,cost[i-2]+T1+T2,cost[i-4]+T1+T2*3)
      elif 2 <= i:
        cost[i] = min(cost[i-1]+T1,cost[i-2]+T1+T2)
      elif i == 1:
        cost[i] = T1
    
print(cost[L])
'''
'''
模範解答
'''

for i in range(L+1):
      if 4 <= i:
        cost[i] = min(cost[i-1]+T1,cost[i-2]+T1+T2,cost[i-4]+T1+T2*3)
      elif 2 <= i:
        cost[i] = min(cost[i-1]+T1,cost[i-2]+T1+T2)
      elif i == 1:
        cost[i] = T1
      if i == h[i]:  #あとから足す方がシンプル
          cost[i] += T3

#ジャンプの途中でゴールした場合
for i in [L-3,L-2,L-1]:
    if i > 0:
        cost[i] = min(cost[i],cost[i]+T1//2+T2*(2*(L-i)-1)//2)

print(cost[L])
