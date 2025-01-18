m = int(input())
n = int(input())
result = []
temp = []
prime_number = [2]
max_value = 0
sum_value = 0

if n == 1 and m == 1:
    print(-1)
    exit(0)
else:
    for i in range (2,n+1):
        flag = True
        for j in (prime_number):
            if i % j == 0:
                flag = False
                break
        if flag == True:
            prime_number.append(i)

    for i in prime_number:
        if m <= i <= n:
            temp.append(i)

    if not temp:
        print(-1)
        exit(0)
    else:
        sum_value = sum(temp)
        min_value = temp[0]

    print(sum_value)
    print(min_value)