n = int(input())
arr = []

for i in range(2,n+1):
    while(n % i == 0):
        n //= i
        arr.append(i)

for i in arr:
    print(i)
