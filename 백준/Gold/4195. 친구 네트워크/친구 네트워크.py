import sys

n = int(sys.stdin.readline())

def find(x):
    if arr[x] != x:
        arr[x] = find(arr[x])
    return arr[x]
        
def union(x, y):
    a = find(x)
    b = find(y)
            
    if a != b:
        arr[b] = a
        size[a] += size[b] 

    return size[a]

for _ in range(n):
    arr = []
    size = []
    temp = int(sys.stdin.readline())
    name = {}
    count = 0

    for i in range(temp):
        s = sys.stdin.readline().split()
        
        if s[0] not in name:
            name[s[0]] = count
            arr.append(count)
            count += 1
            size.append(1)
    
        if s[1] not in name:
            name[s[1]] = count
            arr.append(count)
            count += 1
            size.append(1)
    
        result = union(name[s[0]], name[s[1]])
        print(result)

