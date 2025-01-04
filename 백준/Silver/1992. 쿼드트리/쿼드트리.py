from collections import deque
import sys
q = deque()

n = int(input())

arr = [[] for _ in range (n)]

for i in range (n):
    tmp1 = input()
    
    for j in tmp1:
        arr[i].append(int(j))
# 여기까지 입력을 받는 부분


def divide(brr, mid):
    flag_1 = False # 만약 1이 나오면 True
    flag_0 = False # 만약 0이 나오면 True
    
    if mid == 1:
        if brr[0][0] == 1:
            q.append(1)
        elif brr[0][0] == 0:
            q.append(0)
        return None
    
    for i in range (mid):
        for j in range (mid):
            if brr[i][j] == 1:
                flag_1 = True
            else:
                flag_0 = True
    
    if flag_1 == True and flag_0 == True:
        # 1과 0이 모두 있을때
        # 1과 0이 모두 있다면, 압축이 안되기 때문에
        # 4분할해서 재귀
        mid = mid // 2
        '''
        f_s = brr[:mid][:mid]
        s_s = brr[:mid][mid:]
        t_s = brr[mid:][:mid]
        r_s = brr[mid:][mid:]
        '''
        f_s = [row[:mid] for row in brr[:mid]]  # 왼쪽 위
        s_s = [row[mid:] for row in brr[:mid]]  # 오른쪽 위
        t_s = [row[:mid] for row in brr[mid:]]  # 왼쪽 아래
        r_s = [row[mid:] for row in brr[mid:]]  # 오른쪽 아래
        q.append("(")
        f_sorted = divide(f_s, mid)
        s_sorted = divide(s_s, mid)
        t_sorted = divide(t_s, mid)
        r_sorted = divide(r_s, mid)
        q.append(")")
    
    elif flag_1 == True and flag_0 == False:
        # 1만 존재할 때, 압축 가능
        # 압축이 가능하기 때문에 divide 하지 않고 그대로 압축한 값을
        # q에 추가
        q.append(1)

    else:
        # 0만 존재할 때, 압축 가능
        # 압축이 가능하기 때문에 divide 하지 않고 그대로 압축한 값을
        # q에 추가
        q.append(0)

divide(arr, n) # 처음 함수 입력값, arr 전체 배열과 확인해야 하는 범위
               # n 전체

for i in q:
    print(i, end ="")