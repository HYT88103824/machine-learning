#集合×全探索の問題

N = int(input())
happiness = []

for i in range(N-1):
    row = list(map(int,input().split()))
    happiness.append([0]*(i+1)+row)

#集合を整数として考える
ALL = 1<<N #2進数で 10000・・・00 = 2**N 集合としてあり得る個数
happy = [0]*ALL

def has_bit(n,i):
    return (n&(1<<i)>0) #整数にも&を適応できる

for n in range(ALL):
    for i in range(N):
        for j in range(i+1,N):
            if has_bit(n,i) and has_bit(n,j):
                happy[n] += happiness[i][j]

ans = -10**100

for n1 in range(ALL):
    for n2 in range(ALL):
        if n1&n2 > 0:
            continue
        n3 = ALL-1 - (n1|n2) #ALL = 2**n-1
        ans = max(ans,happy[n1]+happy[n2]+happy[n3])
        
print(ans)