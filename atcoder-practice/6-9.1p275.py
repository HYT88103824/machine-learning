A,B,X = map(int,input().split())

left,right = 0,10**9

while left + 1 < right:
    mid = (left+right)//2
    print(mid,left,right)
    d = len(str(mid))
    
    if A*mid + B*d < X:
        left = mid
    else:
        right = mid

print(left)