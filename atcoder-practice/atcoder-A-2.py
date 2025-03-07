aoki_total = 0
takahashi_total = 0

match_number = int(input())
while match_number>=100:
    match_number = int(input())
    
for x in range(1,match_number+1):
    takahashi_point, aoki_point = map(int,input().split())
    takahashi_total += takahashi_point
    aoki_total += aoki_point
    
if takahashi_total > aoki_total:
    print('takahashi')
elif aoki_total > takahashi_total:
    print('aoki')
else:
    print('draw')
    