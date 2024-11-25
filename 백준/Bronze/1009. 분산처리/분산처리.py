n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    tmp = 1
    a %= 10
    
    while b > 0:
        if b % 2 == 1:
            tmp = (tmp * a) % 10
        a = (a * a) % 10
        b //= 2
            
    if tmp == 0:
        print(10)
    else:
        print(tmp)
