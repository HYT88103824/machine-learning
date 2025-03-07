'''
N = int(input())
num = list(map(int,input().split()))
Q = int(input()) 
Query = []
count = 0

for i in range(Q):
    q = []
    q = list(map(int,input().split()))
    Query.append(q)
    
for q in Query:
    if q[0]==1:
        if num[q[1]-1] >= q[2]:
            count += q[2]
            num[q[1]-1] -= q[2]
    if q[0] == 2:
        judge = True
        for i in range(0,N,2):
            if num[i] < q[1]:
               judge = False
        if judge:
            if N%2 == 0:
              count += q[1]*(N/2)
            if N%2 != 0:
              count += int(q[1]*(N//2+1))
            for i in range(0,N,2):
                num[i] -= q[1]
    if q[0] == 3:
        check = True
        for i in range(N):
             if num[i] < q[1]:
                 check = False
        if check:
            count += q[1]*N
            for i in range(N):
                num[i] -= q[1]
                
print(int(count))
'''

'''
TLEを考慮した高速なコード
'''
N = int(input())
C = list(map(int,input().split()))
Q = int(input()) 
Query = []
sell = 0
z = 0
s = 0

min_s_C = 1000000000
min_z_C = 1000000000

for i in range(N):
    if i%2 == 0:
        min_s_C = min(C[i],min_s_C)
    else:
        min_z_C = min(C[i],min_z_C)

for _ in range(Q):
    query = list(map(int,input().split()))
    
    if query[0] == 1:
        x = query[1]-1
        a = query[2]
        
        if x%2 == 0:
            card_x = C[x]-z-s
        else:
            card_x = C[x]
        
        if card_x >= a:
          C[x] -= a
          sell += a
        
          if x%2 == 0:
            min_s_C = min(C[x],min_s_C)
          else:
            min_z_C = min(C[x],min_z_C)  
    elif query[0] == 2:
        a = query[1]
        
        if min_s_C-s-z >= a:
            s+=a
    elif query[0] == 3:
        a = query[1]
        
        if min(min_s_C-s-z,min_z_C-z) >= a:
            z += a

for i in range(N):
    if i%2 == 0:
        sell += s
        
sell += z*N

print(sell)
            