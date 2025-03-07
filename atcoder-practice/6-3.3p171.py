'''
DFS
'''
from collections import deque

N = int(input())

ans = 0

def dfs(n,use3,use5,use7):
    global ans
    
    if n > N:
        return
    
    if use3 and use5 and use7:
        ans+=1
    
    dfs(10*n+3,True,use5,use7)
    dfs(10*n+5,use3,True,use7)
    dfs(10*n+7,use3,use5,True)
    

dfs(0,False,False,False)

print(ans)

'''
BFS
'''
N = int(input())
Q = deque([3,5,7])
count = 0  
     
while Q:
    n = Q.popleft()
    if n > N:
        break
    if all(str(n).count(digit)>0 for digit in '357'): #3,5,7全ての個数が1以上
        count +=1
    for x in [3,5,7]:
        Q.append(n*10+x)  # <-deque([5,7,33])<- のように3つずつ数字が入る


print(count)