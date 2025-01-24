n = int(input())

arr = list(map(int, input().split()))
count = 0
result = 0
for i in range (n):
    if arr[i] == 1 :
        count += 1
    else:
        count = 0
    result += count
    
print(result)