# heapq 는 기본적으로 최소힙
from heapq import heappush, heappop
import sys
arr = []
# 0이 들어오는 횟수만큼 답을 출력
n = int(input())
for _ in range (n):
    tmp = int(sys.stdin.readline())
    if tmp == 0:
      if len(arr) == 0:
         print(0)
      else:
         print(heappop(arr))
    else:
       heappush(arr, tmp)
