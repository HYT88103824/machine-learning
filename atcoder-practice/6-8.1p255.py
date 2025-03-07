N = int(input())


task = []
for i in range(N+1):
    task.append([])

for i in range(N):
    A,B = map(int,input().split())
    task[A].append(B)

task[1].sort() #list.sort()->対象をソートする new_list = sorted(list)

#list.sort(reverse = True)
#new_list = sorted(list,reverse=True)

ans = 0
for i in range(1,N+1):
    if i == N:
        ans += max(task[N])
        print(ans)
    else:
     ans += max(task[i])
     print(ans)
     task[i][len(task[i])-1] = 0
     task[i+1].extend(task[i])
     task[i+1].sort()
    

#貪欲法
#最良でない方法を選択したとしてもそこを修正できることが必要