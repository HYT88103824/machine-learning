'''
数学的分析に基づく解法
'''
'''
S = input()
count = 0
str_count= 0
judge = True

if len(S)>= 3:
  count += 7*(len(S)-2)+1


for x in range(len(S)):
  for i in range(len(S)):
    if x == i:
        judge = True
    elif S[x] != S[i]:
        judge = True
    else:
        judge = False
  str_count += 1

count += (str_count+1)*2+1

print(count)
'''
'''
全探索
'''
S = input()
c_1 = 0
c_2 = 0
c_3 = 0

def check(letter):
    for i in range(len(S)-len(letter)+1):
        judge = True
        for t in range(len(letter)):
           if S[i+t] != letter[t] and letter[t] != ".":  #否定条件にしないと1文字目が一致しただけでjudgeがTrueに変わってしまう
               judge = False                             #すべて一致でTrueの時は否定条件でデフォルトから変更するようにする 
        if judge:
          return 1
    return 0
               

alpha = "abcdefghijklmnopqrstuvwxyz."


for x in alpha:
    if check(x):
        c_1 += 1
     
for x in alpha:
    for y in alpha:
        str_2 = x+y
        if check(str_2):
            c_2 += 1
  
for x in alpha:
    for y in alpha:
        for z in alpha:
            str_3 = x+y+z
            if check(str_3):
                c_3 += 1

count = c_1+c_2+c_3
print(count)