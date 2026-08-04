from collections import deque

def solution(priorities, location):
    answer = 0
    count = 0
    q = deque(enumerate(priorities)) # (현재 위치, 우선순위) 인덱스와 함께 저장
    while q:
        idx, prior = q.popleft()
        flag = True
        j = 0
        while (j < len(q)):
            if prior < q[j][1]:
                q.append((idx, prior))
                flag = False
                break
            j += 1
            
        if flag:
            count += 1
            if idx == location : answer = count
            
    return answer
        
        