import sys
n = int(input())
arr = []
for _ in range (n):
    tmp = int(sys.stdin.readline())
    arr.append(tmp)

arr.sort()
for i in arr:
    print(i)