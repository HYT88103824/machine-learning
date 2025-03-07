import math

left = 0
right = 2.001


while left + 0.000001 < right:
    mid = (left+right)/2
    
    if mid**2 < 3:
        left = mid
    elif mid**2 > 3:
        right = mid
    else:
        break
    
print(left,right)

left = 0
right = math.pi+0.001

while left + 0.000001 < right:
    mid = (left+right)/2
    
    if mid < math.pi:
        left = mid
    elif mid > math.pi:
        right = mid
    else:
        break
    
print(left,right)