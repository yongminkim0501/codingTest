n, b = map(int, input().split())
arr = []

while (n > 0):
    if n % b >= 10:
        tmp = chr(n % b + 55)
        arr.append(tmp)
    else:
        arr.append(str(n % b))
    n //= b

print(''.join(arr[::-1]))