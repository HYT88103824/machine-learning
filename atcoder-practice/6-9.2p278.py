R,B = map(int,input().split())
x,y = map(int,input().split())


left = 0
right = 10**18+1

while abs(left-right) > 1:
    mid = (left+right)//2
    r = R-mid                  #どの組でも赤と青のバラを1本ずつ使うので引く
    b = B -mid    
    if r >= 0 and b >= 0:
        count = r//(x-1) + b//(y-1)  #残ったバラからできる組数を計算
        if mid <= count:
            left = mid
        else:
            right = mid
    else:
        right = mid
    
    
print(left)

#全体
#BBBBB
#RRRRR

#x = 3,y = 4

#mid = 3
#
#1本ずつ  残り
#
#  BBB 　 BR    残りからR2つを追加すると1組だけできる
#  RRR    BR

#mid = 2
#1本ずつ  残り
#         BR
#  BB 　  BR    残りからR2つまたはB3つを追加すると2組できる
#  RR     BR