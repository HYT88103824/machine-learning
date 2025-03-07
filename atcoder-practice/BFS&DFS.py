'''
BFS
'''
import sys
from collections import deque
sys.setrecursionlimit(1000000)

N = 9
s = 0
E = [[2,3],[1,4,5],[1,6],[2,7],[2],[3,8,9],[4],[6],[6]]


visited = []
for i in range(N):
    visited.append(False)

Q = deque()
Q.append(s)
visited[s]= True

while len(Q) > 0:
    i = Q.popleft()
    for j in E[i]:
        j -= 1
        if not visited[j]:
            visited[j] = True
            Q.append(j)

'''
DFS
'''

visited = []
for i in range(N):
    visited.append(False)

def dfs(i):
    visited[i] = True
    for j in E[i]:
        j-=1
        if not visited[j]:
            dfs(j)

dfs(s)