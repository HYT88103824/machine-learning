N = int(input())
height = list(map(int,input().split()))

def transfer(position,cost):
  if position == N-1:
      print(cost)
  elif position == N-2:
      cost += abs(height[N-2]-height[N-1])
      position += 1
      transfer(position,cost)
  else:
    if abs(height[position]-height[position+1]) < abs(height[position]-height[position+2]):
      cost += abs(height[position]-height[position+1])
      position += 1
      transfer(position,cost)
    elif abs(height[position]-height[position+1]) == abs(height[position]-height[position+2]):
      cost += abs(height[position]-height[position+1])
      position += 2
      transfer(position,cost)
    else:
      cost += abs(height[position]-height[position+2])
      position += 2
      transfer(position,cost)

transfer(0,0)

'''
模範解
'''
N = int(input())
h = list(map(int,input().split()))

cost = [0]*N

cost[1] = cost[0]+abs(h[0]-h[1])

for i in range(2,N):
    cost[i] = min(cost[i-1]+abs(h[i]-h[i-1]),cost[i-2]+abs(h[i]-h[i-2]))
    
print(cost[N-1])