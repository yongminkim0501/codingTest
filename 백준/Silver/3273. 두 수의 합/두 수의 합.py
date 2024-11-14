from collections import defaultdict

input_n = int(input())
a = list(map(int, input().split()))
input_x = int(input()) 

count = 0
freq = defaultdict(int)

for num in a:
    count += freq[input_x - num]
    freq[num] += 1

print(count)