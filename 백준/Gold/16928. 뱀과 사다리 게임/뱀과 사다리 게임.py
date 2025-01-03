from collections import deque

def bfs(n, m, l, s):
    visit = [False] * 101
    d = [0] * 101
    
    b = {}
    for x, y in l:
        b[x] = y
    for u, v in s:
        b[u] = v
    
    q = deque([1])
    visit[1] = True
    
    while q:
        cur = q.popleft()
        
        if cur == 100:
            return d[100]
            
        for dice in range(1, 7):
            np = cur + dice
            
            if np > 100 or visit[np]:
                continue
                
            if np in b:
                np = b[np]
            
            if not visit[np]:
                visit[np] = True
                d[np] = d[cur] + 1
                q.append(np)
                
    return -1

n, m = map(int, input().split())
l = [tuple(map(int, input().split())) for _ in range(n)]
s = [tuple(map(int, input().split())) for _ in range(m)]

print(bfs(n, m, l, s))