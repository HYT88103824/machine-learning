H,W = map(int,input().split())

grid = []
for i in range(H):
    row = input()
    grid.append(row)


check = []
for i in range(H):  
  check.append([True]*W)
  
count = []
for i in range(H):  
  check.append([0]*W)

for i in range(H):
  for j in range(W):
    if grid[i][j] == '.':
      c = 0
      i2 = 0
      j2 = 0
      while 0 <= i2 < H and 0 <= j2 < W:
        for i2,j2 in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
          if 0 <= i2 < H and 0 <= j2 < W:
              if grid[i2][j2] == '#':
                  check[i][j] = False
              else:
                  c += 1
        if check[i][j]:
            count[i][j] += c
        else:
            break
      
      check.append(count[i][j])  

print(max(check))         
                  
                  
    