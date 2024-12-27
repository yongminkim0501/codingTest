n, m = map(int, input().split())
arr = []
brr = []
result = [[] for _ in range(n)]
for i in range(n):
    for j in range(m):
        result[i].append(0)
for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

for i in range(n):
    tmp = list(map(int, input().split()))
    brr.append(tmp)

for i in range(n):
    for j in range(m):
        result[i][j] = arr[i][j] + brr[i][j]

for i in result:
    print(*i)