n, k = map(int, input().split())
arr = []
for i in range(1,n+1):
    if n % i == 0:
        arr.append(i)

if len(arr) >= k:
    print(arr[k-1])
else:
    print(0)