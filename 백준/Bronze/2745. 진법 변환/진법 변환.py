# 'A' = 65 ~ 90
from collections import deque
a1, b = input().split()

a = deque((a1))
b = int(b)

string = []
count = 1
result = 0

for i in range (1, 10):
    string.append([str(i), i])

for i in range (65, 91):
    string.append([chr(i), i-55])

d = []
for i in range(len(a)-1, -1, -1):
    d.append(b**i)

result = 0
for i in range(len(a)):
    for j in string:
        if a[i] == j[0]:
            result += d[i]*j[1]
            break 

print(result)
'''

count = 35*36**4 + 35*36**3 + 35*36**2 + 35*36**1 + 35*1
print(count)'''