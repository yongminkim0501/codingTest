import sys
sys.setrecursionlimit(10**5)

n,m,r = map(int, sys.stdin.readline().split())
arr = [[] for _ in range (n+1)]
visit = [0] * (n+1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)

for i in range(n):
    arr[i].sort()

count = 1
def dfs(arr, x, visit):
    global count
    visit[x] = count
    for i in arr[x]:
        if visit[i] == 0:
            count += 1
            dfs(arr, i, visit)

# 시작 정점 : r
dfs(arr, r, visit)

for i in range(1, n+1):
    print(visit[i])