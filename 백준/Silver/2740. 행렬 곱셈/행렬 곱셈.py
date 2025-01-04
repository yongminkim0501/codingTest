import sys

n, m = map(int, sys.stdin.readline().split())
arr = [[] for _ in range (n)]
for i in range(n):
    tmp = list(map(int,sys.stdin.readline().split()))
    arr[i] = tmp

a, b = map(int, sys.stdin.readline().split())
brr = [[] for _ in range(a)]
for i in range(a):
    tmp = list(map(int, sys.stdin.readline().split()))
    brr[i] = tmp
crr = [[0 for _ in range(b)] for _ in range(n)]
for i in range(n): 
    for j in range(b):
        for k in range(m):
            crr[i][j] += arr[i][k] * brr[k][j]

for i in range(n):
    print(*crr[i])
