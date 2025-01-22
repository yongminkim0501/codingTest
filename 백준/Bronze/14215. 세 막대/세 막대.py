a, b, c = map(int, input().split())

arr = [a,b,c]

arr.sort()

print(arr[0] +arr[1] + min(arr[2],(arr[0]+arr[1]-1)))
