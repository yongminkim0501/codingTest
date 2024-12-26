import sys 
from collections import deque

n, m, r = map(int, sys.stdin.readline().split())
arr = [[] for _ in range (n+1)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)

q = deque()
result = [0]*(n+1)


for i in arr:
    i.sort(reverse=True)
count = 1

def bfs(v,r):
    global count
    visit = [0]*len(v)
    visit[r] = 1
    result[r] = count
    q.append(r)
    while(len(q) != 0):
        tmp = q.popleft()
        for j in arr[tmp]:
            if visit[j] == 0:
                count += 1
                visit[j] = 1
                result[j] = count
                q.append(j)
        
'''
for i in arr[tmp]:
    tmp += 1

for i in arr:
    for j in i:        
'''


bfs(arr,r)

for i in range(1, n+1):
    print(result[i])