N = int(input())
S = []
for i in range(0,N):
  row  = input()
  row = list(row)  #pythonでは文字列は変換できない->文字列をリストに変換
  S.append(row)

for x in range(N-2,-1,-1):
    for y in range(1,2*N-1):
        if S[x][y] == '#':
          if S[x+1][y-1] =='X':
              S[x][y] = 'X'
          if S[x+1][y] =='X':
              S[x][y] = 'X'
          if S[x+1][y+1] =='X':
              S[x][y] = 'X'


for i in range(0,N):
    S[i] = ''.join(S[i])
    print(S[i])