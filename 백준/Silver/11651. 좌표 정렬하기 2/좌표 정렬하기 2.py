#arr.sort(key = lambda x:(x[0],x[1]))
import sys
n = int(input())
arr = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    arr.append([a,b])


arr.sort(key=lambda x:(x[1], x[0]))

for i in arr:
    print(i[0], i[1])