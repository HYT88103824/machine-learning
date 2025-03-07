N,K = map(int,input().split())
A = list(map(int,input().split()))


left,right = 0,len(A)-1

while right-left > 1:
        mid = (left+right)//2
        
        if K <= A[mid]:
            right = mid
        else:
            left = mid
    
if right == len(A)-1:
    print(-1)
else:
    print(right)