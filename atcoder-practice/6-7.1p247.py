#リーダーの方向を向くというのはリーダが向いている方向を向くという意味ではなくリーダーが'いる'方向を向くという意味である

N = int(input())
S = input()

count = [[0,0]]
se = 0
sw = 0

for i in range(N):
    if S[i] == 'E':
        se += 1
    else:
        sw += 1
    count.append([se,sw])

print(count)
min = 10**18

for i in range(1,N+1):
    c = count[i-1][1] + count[N][0] - count[i][0]
    if c < min:
        min = c

print(min)

    