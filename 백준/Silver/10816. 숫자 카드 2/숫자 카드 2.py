'''
숫자 카드는 정수 하나가 적혀져 있는 카드
상근이는 숫자 카드 n개를 가지고 있음.
정수 m개가 주어졌을 때, 이 수가 적혀있는 숫자카드를 상근이가 몇 개 가지고 있는지
'''
import sys
n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
m = int(input())
brr = list(map(int, sys.stdin.readline().split()))
result = []
count_d = {}
for num in arr:
    if num in count_d:
        count_d[num] += 1
    else:
        count_d[num] = 1

for num in brr:
    result.append(count_d.get(num,0))

print(*result)