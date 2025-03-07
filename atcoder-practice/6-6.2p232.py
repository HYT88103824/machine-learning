N = int(input())
count = 0

for c in range(1,N):
    for b in range(1,N-c+1):
            a = (N-c)/b
            if a > 0 and a.is_integer():
                count += 1

print(count)

ans = 0
         
for A in range(1,N):
    b_count = (N-1)//A
    ans += b_count
    
print(ans)