'''
ABCDE
abcde
01234
FGHIJ
fghij

AABCDD
afzz
09121
a8EWg6
P5h3kx
'''
from collections import deque
count = 0
arr = deque()
for i in range (5):
    tmp1 = input()
    tmp = deque(tmp1)
    arr.append(tmp)
    count += len(arr[i])

result = []

while(count > 0):
    count -= 1
    for i in range(5):
        if len(arr[i]) != 0 :
            result.append(arr[i].popleft())

for i in result:
    print(i, end ="")