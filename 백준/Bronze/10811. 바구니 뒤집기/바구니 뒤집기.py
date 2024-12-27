n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(i+1)

for i in range(m):
    x,y = map(int, input().split())
    x,y = x-1, y-1
    arr[x:y+1] = reversed(arr[x:y+1])


print(*arr)
