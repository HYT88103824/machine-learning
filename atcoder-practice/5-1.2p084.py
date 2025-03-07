row = []
C = []

for i in range(3):
    row = list(map(int,input().split()))
    C.append(row)
    

if C[0][0]-C[0][1] == C[1][0]-C[1][1] == C[2][0]-C[2][1] and C[0][1]-C[0][2] == C[1][1]-C[1][2] == C[2][1]-C[2][2]:
    neighbor_1 = True
    
if C[0][0]-C[1][0] == C[0][1]-C[1][1] == C[0][2]-C[1][2] and C[1][0]-C[2][0]==C[1][1]-C[2][1]==C[1][2]-C[2][2]:
    neighbor_2 = True

if neighbor_1 and neighbor_2:
    print('Yes')
else:
    print('No')