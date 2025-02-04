n,m = map(int, input().split())
result = n*m

arr = list(map(int, input().split()))

for i in range(len(arr)):
    arr[i] -= result
    
print(*arr)