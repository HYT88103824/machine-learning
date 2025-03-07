bingo = []

for i in range(3):
    bingo_line = []
    bingo_line = list(map(int,input().split()))
    bingo.append(bingo_line)
    


def check(num,new_bingo):
    newer_bingo = []
    for x in new_bingo:
        line = 0
        for y in x:
            line += 1
            if y == num:
                x[line-1] = 0
        newer_bingo.append(x)
    return newer_bingo

def bingo_check(list):
    count = 0
    count_0 = 0
    count_1 = 0
    count_2 = 0
    count_cross_1 = 0
    count_cross_2 = 0
    for x in list:
        count += 1
        if max(x) == 0:
          print('Yes')
          return
        count_0 += x[0]
        count_1 += x[1]
        count_2 += x[2]
        count_cross_1 += x[count-1]
        count_cross_2 += x[3-count]
        
    if count_0 == 0 or count_1 == 0 or count_2 == 0:
        print('Yes')
        return
    if count_cross_1 == 0 or count_cross_2 == 0:
        print('Yes')
        return
    else:
        print('No') 
        return
    
    
N = int(input())
num = int(input())
bingo_before = check(num,bingo)

for x in range(N-1):
  num = int(input())
  bingo_before = check(num,bingo_before)


bingo_check(bingo_before)