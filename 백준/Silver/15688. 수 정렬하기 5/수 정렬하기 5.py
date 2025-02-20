import sys
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    temp = int(input())
    arr.append(temp)

arr.sort()
for i in arr:
    print(i)