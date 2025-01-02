from collections import deque

n, m = map(int, input().split())
visit = [0] * 100001

# 수빈이는 현재 점 n에 있음, 동생은 점 k에 있음.
# 수빈이가 위치가 x일 때 걷는다면 1초 후 위치는 x-1, x+1로 이동
# 순간 이동을 할 경우에는 2*x의 위치로 이동
# 동생은 이동 안함?
q = deque()
q.append(n)
visit[n] = 1
nx = [-1, 1, 2]
def bfs():
    while q:
        x = q.popleft()
        
        for i in range(3):
            if i == 2:
                dx = x*nx[i]
            else:
                dx = nx[i] + x
            # 여기까지가 움직일 수 있는 부분

            if 0 <= dx <= 100000 and visit[dx] == 0:
                if dx == m:
                    visit[dx] = visit[x] + 1
                    print(visit[dx]-1)
                    exit(0)
                else:
                    visit[dx] = visit[x] + 1
                    q.append(dx)

if n == m:
    print(0)
    exit(0)
bfs()
'''
if n == m:
    print(0)
elif m == 0:
    print(visit[0])
else:
    print(visit[m]-1)'''

#print(visit[m])