n = int(input())

count = 0
for i in range(1, 500):
    a = (i**2 + n)**0.5
    if a%1 == 0:
        count += 1
print(count)