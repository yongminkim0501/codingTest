for _ in range (3):
    n = int(input())
    a = 0
    for i in range (n):
        tmp = int(input())
        a += tmp
    if a == 0 :
        print(0)
    elif a > 0 :
        print("+")
    else:
        print("-")