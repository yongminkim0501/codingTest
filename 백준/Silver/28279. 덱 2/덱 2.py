from collections import deque
import sys
'''
1 X: 정수 X를 덱의 앞에 넣는다. (1 ≤ X ≤ 100,000)
2 X: 정수 X를 덱의 뒤에 넣는다. (1 ≤ X ≤ 100,000)
3: 덱에 정수가 있다면 맨 앞의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
4: 덱에 정수가 있다면 맨 뒤의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
5: 덱에 들어있는 정수의 개수를 출력한다.
6: 덱이 비어있으면 1, 아니면 0을 출력한다.
7: 덱에 정수가 있다면 맨 앞의 정수를 출력한다. 없다면 -1을 대신 출력한다.
8: 덱에 정수가 있다면 맨 뒤의 정수를 출력한다. 없다면 -1을 대신 출력한다.
'''

n = int(sys.stdin.readline().rstrip())
que = deque()
for i in range(n):
    tmp = list(map(int, sys.stdin.readline().rstrip().split()))
    if len(tmp) == 2:
        if tmp[0] == 1:
            que.appendleft(tmp[1])
        else:
            que.append(tmp[1])
    else:
        if tmp[0] == 3:
            if len(que) == 0 :
                print(-1)
            else:
                print(que.popleft())
        elif tmp[0] == 4:
            if len(que) == 0:
                print(-1)
            else:
                print(que.pop())
        elif tmp[0] == 5:
            print(len(que))
        elif tmp[0] == 6:
            if len(que) == 0:
                print(1)
            else:
                print(0)
        elif tmp[0] == 7:
            if len(que) == 0 :
                print(-1)
            else:
                print(que[0])
        else:
            if len(que) == 0:
                print(-1)
            else:
                print(que[-1])

