import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())
queuestack = list(map(int, sys.stdin.readline().rstrip().split()))
b = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
tmp = list(map(int, sys.stdin.readline().rstrip().split()))
# 큐면, 그 차례에 원래 있던 게 움직임
# 스택이면, 본인이 움직임
# 즉, 큐면 업데이트
# 스택이면, 패스 ?
# 시간 초과가 났다는 것은, 방식은 같지만 구조를 바꿔야 함.
# q면, temp값을 바꿈
# stack면, 그대로 
temp = deque()
for i in range(n):
    if queuestack[i] == 0:
        temp.append(b[i])
result = []
for i in range(m):
    temp.appendleft(tmp[i])
    result.append(temp.pop())

print(*result)   