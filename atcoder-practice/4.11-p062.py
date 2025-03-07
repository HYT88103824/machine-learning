S = input()
list = []
number = []
count_a=0
count_b=0
count_c=0

print(S)

for x in S:
    list.append(x)

for y in list:
    if y == 'a':
        count_a += 1
    if y == 'b':
        count_b += 1
    if y == 'c':
        count_c += 1
'''
count_a = S.count('a')
count_b = S.count('b')
count_c = S.count('c')
count()で文字の個数を数える
'''
        
if count_a > count_b and count_a > count_c:
    print('a')
if count_b > count_a and count_b > count_c:
    print('a')
if count_c > count_b and count_c > count_a:
    print('a')
'''
max_count = max(count_a,count_b,count_c)
に一致するものを選べばよい
'''