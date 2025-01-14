'''
n개가 주어졌을 때,
i번째 수부터 j번째 수까지 합을 구하는 프로그램

첫째 줄에 수의 개수 n과 합을 구해야 하는 횟수 m이 주어짐.
둘째 줄에는 n개의 수가 주어진다.
셋째 줄에는 구해야 하는 구간 i와 j가 주어진다.
'''
import sys
n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
sum_arr = [0] * (n+1)
for i in range (n):
    sum_arr[i+1] = sum_arr[i] + arr[i]

for _ in range(m):
    count = 0
    i, j = map(int, sys.stdin.readline().split())

    print(sum_arr[j]-sum_arr[i-1])