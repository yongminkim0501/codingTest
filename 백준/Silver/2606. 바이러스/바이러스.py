import sys 
from collections import deque
'''
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
bfs(arr,r)

for i in range(1, n+1):
    print(result[i])
'''
n = int(input())
m = int(input())
arr = [[] for _ in range (n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)

q = deque()
result = [0]*(n+1)
visit = [0]*(n+1)
def bfs(v,r):
    visit[r] = 1
    result[r] = 1
    q.append(r)
    while(len(q)!= 0):
        tmp = q.popleft()
        for i in arr[tmp]:
            if visit[i] == 0:
                visit[i] = 1
                q.append(i)
                result[i] = 1
bfs(arr, 1)

count = 0
for i in result:
    if i != 0:
        count += 1
print(count-1)

