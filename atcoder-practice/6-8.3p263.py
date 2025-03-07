'''
N = int(input())

dish = []
for i in range(N):
    A,B = map(int,input().split())
    dish.append([A-B,A,B])             #選んだ料理を2人とも食べるわけではないので差を考えても意味はない

dish.sort()

t = 0
a = 0
for i in range(N):
    if i%2 == 0:
      t += dish[-1][1] 
      dish.pop(-1)  
    else:
      a += dish[-1][2]   
      dish.pop(0) 

print(t-a)
'''
N = int(input())

dish = []
for i in range(N):
    A,B = map(int,input().split())
    dish.append([-A-B,A,B])    

dish.sort()

t = 0
a = 0
for i in range(N):
    if i%2 == 0:
      t += dish[0][1] 
      dish.pop(0)
    else:
      a += dish[0][2]
      dish.pop(0)   

print(t-a)
