K = int(input())
list = list(map(int,input().split()))
A = list[0]
B = list[1]

for x in range(A,B+1):
    if x%K == 0:
        judge = True
        break
    else:
        jubge = False

if judge:
    print('OK')
else:
    print('NG')