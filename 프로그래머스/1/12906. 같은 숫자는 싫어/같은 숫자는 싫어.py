from collections import deque

def solution(arr1):
    arr = deque(arr1)
    stk = deque()
    stk.append(arr[0])
    arr.popleft()
    if len(stk) == 0 :
        stk.append(arr[0])
        arr.popleft()
    else:
        for item in arr :
            if not stk[-1] == item:
                stk.append(item)
    
    return list(stk)
