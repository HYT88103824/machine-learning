'''
剰余を使う方法
'''

N = int(input())
divided_N = N//9  #math.ceil(N/9)とすると18/9=2 15/9=1.66=>2 となるので便利
reminder_N = N%9
list = []

if reminder_N == 0:
    reminder_N = 9
    divided_N -= 1

for i in range(divided_N+1):  #1,2,3,4,5,6,7,8,9もゾロ目に入るものとする
      list.append(reminder_N)
    
joint_list = "".join(str(x) for x in list)    
print(joint_list)     
      
'''
全探索
'''
N = int(input())
count = 0

for x in range(1,555555+1):
    list = []
    judge = False
    for y in str(x):
     list.append(int(y))
    
    if max(list) == min(list):
        count += 1
        judge = True
    if count == N and judge:
        joint = ''.join(str(z) for z in list)
        print(joint)