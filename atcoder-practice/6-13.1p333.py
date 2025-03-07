#10/33accept
#TLEとWAも出た

'''
from collections import deque
Q = int(input())

query = []
for i in range(Q):
    q = input().split()
    query.append(q)

alpha = 'abcdefghijklmnopqrstuvwxyz'

dq = deque('#')

for x in query:
    
    if int(x[0]) == 1:
        for i in range(int(x[2])):
           dq.append(x[1])
        dq.append('#')
    
    if int(x[0]) == 2:
        sum = 0
        de = ''
        st = [0]*27
        for j in range(int(x[1])):
          if len(dq) == 0:
            break
          s = dq.popleft()
          de += s
          if s == '#':
              if len(dq)==0:
                  break
              count = 0
              s = dq.popleft()
              for x in alpha:
                  count += 1
                  if s == x:
                   break
          st[count] += 1
                       
        for i in range(27):
          sum += (st[i])**2
        print(sum)
'''
from collections import deque
from string import ascii_lowercase

Q = int(input())
que = deque()

for q in range(Q):
    values = input().split()
    
    if values[0] == '1':
        c = values[1]
        x = int(values[2])
        que.append([c,x])
    else:
        d = int(values[1])
        cnt = {}            #辞書型
        
        for c in ascii_lowercase: #アルファベット呼び出し
            cnt[c] = 0
        
        while d > 0 and len(que) > 0:
            c,x = que[0]
            if d >= x:
                d -= x
                cnt[c] += x
                que.popleft()
            else:
                cnt[c] += d
                que[0][1] -= d
                d = 0
        ans = 0
        for c in ascii_lowercase:
            ans += cnt[c]**2
        print(ans)