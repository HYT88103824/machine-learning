'''
隣接行列
'''
N,Q = map(int,input().split())
matrix = []
log = []

for i in range(N):
    row = []
    for j in range(N):
        row.append(False)
    matrix.append(row)


for i in range(Q):
    line = list(map(int,input().split()))
    log.append(line)
    
for x in log:
    if x[0] == 1:
        matrix[x[1]-1][x[2]-1] = True

    if x[0] == 2:
        for i in range(N):
            if matrix[i][x[1]-1]:
                matrix[x[1]-1][i] = True
                
    if x[0] == 3:
        follow = []
        for i in range(N):
            if matrix[x[1]-1][i]: 
              for j in range(N):
                if matrix[i][j] and j != x[1]-1: 
                    follow.append(j)
        for w in follow:
          matrix[x[1]-1][w] = True
#フォロワー１がフォロワー3をフォローしたことにより
#フォロワー3がフォローしている人(フォロワー4)もフォローしてしまっている


YN = []
for x in matrix:
    row = []
    for y in x:
     if y:
        row.append('Y')
     if not y:
        row.append('N')
    YN.append(row)

for x in YN:
    joint = ''.join(x)
    print(joint)


#NYNNYN    NYYNYN     NYYYYN 1が3のフォロワーをフォロー
#NNYNNN    NNYNNN     NNYNNN してしまう.本来は2と5のみ.
#NNNYNN => NNNYNN　=> NNNYNN
#NNNNNN    NNNNNN     NNNNNN
#NNNNNY    NNNNNY     NNNNNY
#NNNNNN    NNNNNN     NNNNNN                 
# 5個目  1が2のフォロワー
#        をフォロー