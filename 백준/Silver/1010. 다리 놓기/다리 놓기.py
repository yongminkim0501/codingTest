import sys
n = int(input())
count = 1
def fac(x):
    result = 1
    for i in range(x):
        result *= (i+1)
    return result
for i in range(n):
    a, b = map(int,sys.stdin.readline().split())
    c = fac(a)
    d = fac(b)   
    n_r = fac(b-a)
    re = d/(c*n_r)
    print(int(re))

# 첫번째가 선택할 수 있는 것, b - a + 1