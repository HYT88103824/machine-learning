A,B,C = map(int,input().split())
    
total = 0

for a in range(1,A+1):
    for b in range(1,B+1):
        for c in range(1,C+1):
            total += a*b*c

print(total%998244353)

D = A*(A+1)//2
E = B*(B+1)//2
F = C*(C+1)//2

print((D*E*F)%998244353)
