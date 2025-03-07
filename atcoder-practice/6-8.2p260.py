N = int(input())

task = []

for i in range(N):
    A,B = map(int,input().split())
    task.append([B,A])

task.sort() #ソートは多次元リストの場合は最初の要素で比較される


deadline = 0
count = 0
for i in range(N):
    if deadline < task[i][1]:
      deadline = task[i][0]
      count +=1

print(count)

