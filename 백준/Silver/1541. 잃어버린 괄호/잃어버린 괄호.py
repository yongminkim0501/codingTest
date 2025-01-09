from collections import deque
n = input()
tmp = ""
q = deque()
for i in range(len(n)):
    if n[i] == '-' or n[i] == '+':
        q.append(int(tmp))
        q.append(n[i])
        tmp = ""
    else: 
        tmp += n[i]

    if i == len(n)-1:
        q.append(int(tmp))

value = 0
flag = True
tmp_flag = True
for i in q:
    if i == '-' and flag == True:
        flag = False # 해당 값이 처음 나온 - 라면, flag를 false로 함
        continue    
    elif i == '-' and flag == False: 
        flag = True # 해당 값이 두번째 나온 - 라면, flag를 True로 함
        tmp_flag = False
        continue
    if i == '+' :
        continue
    if flag == False: # 처음 나온 - 이후 나온 숫자라면 전부 value에서 뺌
        value -= i
    else: # true 라면, 괄호 안에 값이 아니기 때문에 value에서 더함
        if tmp_flag == False:
            value -= i
        else:
            value += i

print(value)