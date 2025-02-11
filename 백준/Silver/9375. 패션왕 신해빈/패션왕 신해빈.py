import sys
'''
한 번 입었던 옷들의 조합을 절대 다시 입지 않는다.
예를 들어 오늘 해빈이가 안경, 코트, 상의, 신발을 입었다면
바지를 추가로 입거나 안경 대신 렌즈를 착용하거나 해야함.
'''

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    name = []
    result = {}

    n = int(input())

    for i in range (n):
        a,b = input().split()
        if b not in name:
            name.append(b)
            result[b] = 1
        else:
            result[b] += 1

    count = 1
    if len(name) == 1:
        count = 0
        for i in name:
            count += result[i]
        print(count)
    else:
        for i in name:
            count *= result[i]+1
        print(count - 1)