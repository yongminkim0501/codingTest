m, n = map(int, input().split())
result = []

def isPrime(a):
    flag = True
    if a < 2:
        flag = False
        return flag
    for i in range(2, int(a**0.5)+1):
        if (a%i == 0):
            flag = False
            return flag
    if flag == True : result.append(a)
    return True

for i in range(m,n+1):
    if isPrime(i) :
        print(i)