'''
N,X = map(int,input().split())

weight = []
for i in range(N):
    w = int(input())
    weight.append(w)
    
center = len(weight)//2
left = weight[:center]
right =weight[center:]

print(left,right)


def cal(list,num,sum):
  cost = []
  for x in range(num+1):
      cost.append([0]*(sum+1))
  cost[0][0] = 1
  list.insert(0,0)
  for i in range(1,num+1):
     for j in range(sum+1):
        if j-list[i]>=0:
           cost[i][j] = cost[i-1][j-list[i]] or cost[i-1][j]
        else:
           cost[i][j] = cost[i-1][j]
  print(cost)
      
  return cost

cost_l = cal(left,len(left),sum(left))[len(left)-1]
cost_r = cal(right,len(right),sum(right))[len(right)-1]


count = 0
for x in range(len(cost_l)):
    if cost_l[x] == 1:
      for y in range(len(cost_r)):
        if cost_r[y] == 1 and x+y == X:
              count += 1
                
print(count)  #この解法だと1のものが2つあるため1+4=5を区別できない
'''
'''
defaultdictについて
https://memoribuka-lab.com/?p=1680
'''
from collections import defaultdict

N,X = map(int,input().split())
A = []
B = []
for i in range(N):
    w = int(input())
    if i%2 == 0:
        A.append(w)
    else:
        B.append(w)

#A = [1,2,4]
#B = [1,3]

def has_bit(n,i):
    return (n&1<<i > 0)

dic = defaultdict(int)

for n in range(1<<len(B)):
    s = 0
    for i in range(N):  #それぞれの集合に対しての重さを計算
        if has_bit(n,i):
            s += B[i]
    dic[s] += 1 #求めた数をkeyとしてvalueにその個数を記録
    
#dic = {0:1,1:1,3:1,4:1}
    
ans = 0
for n in range(1<<len(A)):
    s = 0
    for i in range(N):  
        if has_bit(n,i):
            s += A[i]
    ans += dic[X-s] #合計がXになるものの数を求める

print(ans)

#defaultdictは要素の個数を数えるときに便利