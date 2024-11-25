n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    if a % 10 == 0:
        print(10)
        continue
        
    b = b % 4
    if b == 0:
        b = 4
    
    tmp = a % 10
    for _ in range(b-1):
        tmp = (tmp * a) % 10
        
    if tmp == 0:
        print(10)
    else:
        print(tmp)