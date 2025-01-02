'''
첫 줄에는 상자의 크기를 나타내는 두 정수 m,n 과 상자의 수를 나타내는 H가 주어짐.
m은 상자의 가로 칸의 수, n은 상자의 세로 칸의 수를 나타냄.

둘째 줄부터는 가장 밑의 상자부터 가장 위의 상자까지 저장된 토마토들의 정보가 주어짐
각 줄에는 상자 가로줄에는 들어있는 토마토들의 상태가 m개의 정수로 주어짐
정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1 토마토가 들어있지 않은 칸
n개의 줄이 h번 반복하여 주어짐

토마토가 하나 이상 있는 경우만 입력으로 주어짐

토마토가 모두 익을 때까지 최소 며칠
토마토가 익어있는 상태면 0,
모두 익지 못하는 상황이면 -1

예제 입력 2 :
5 3 2
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0

0 0 0 0 0
0 0 1 0 0
0 0 0 0 0

가로 5, 세로 3, 높이 2

예제 입력 3
4 3 2
1 1 1 1
1 1 1 1
1 1 1 1

1 1 1 1
-1 -1 -1 -1
1 1 1 -1

가로 4, 세로 3, 높이 2
'''
from collections import deque
nx = [-1,1,0,0,0,0]
ny = [0,0,-1,1,0,0]
nh = [0,0,0,0,1,-1] # nx와 ny가 움직임이 0일때 위아래로 움직일 수 있음.

q = deque([])
m,n,h = map(int, input().split())
arr = [[] for _ in range(h)]

for i in range (h):
    for j in range(n):
        tmp = list(map(int,input().split()))
        arr[i].append(tmp)

for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 1:
                q.append([i,j,k])
def bfs():
    while q:
        h1,y1,x1 = q.popleft()
        for tmp in range(6):
            dx = nx[tmp] + x1
            dy = ny[tmp] + y1
            dh = nh[tmp] + h1
            
            if 0<=dx<m and 0<=dy<n and 0<=dh<h and arr[dh][dy][dx] == 0:
                arr[dh][dy][dx] = arr[h1][y1][x1] + 1
                q.append([dh,dy,dx])

bfs()
count = 0
flag = True
for i in range(h):
    for j in range(n):
        for k in arr[i][j]:
            if k == 0:
                flag = False
                break
            count = max(k,count)

if flag == False:
    print(-1)
else:
    print(count-1)
'''
[[[5, 4, 3, 4, 5]
, [4, 3, 2, 3, 4]
, [5, 4, 3, 4, 5]]

, [[4, 3, 2, 3, 4]
, [3, 2, 1, 2, 3]
, [4, 3, 2, 3, 4]]]'''