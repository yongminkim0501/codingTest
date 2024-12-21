from collections import deque
import sys
n = int(sys.stdin.readline().rstrip())

q = deque()
for i in range(n):
    q.append(i+1)

while(True):
    if len(q) == 1:
        print(q[0])
        break
    q.popleft()
    if len(q) == 1:
        print(q[0])
        break
    q.append(q.popleft())



# 한장 남을 때까지 반복
# 제일 위에 있는 카드를 바닥에 버림
# 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮김
