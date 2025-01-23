'''
n = 3인 경우 50을 구하려면
-> 2^3 * 2^3 = 64 (0 ~ 63) 짜리
(0, 1, 2, 3) (3)
여기서 50의 범위가 속하는 곳은 48 <= @ < 64

그럼 다시 48 ~ 63 (16짜리)를 4구간으로 나눔
(0, 1, 2, 3) 1구간 4짜리
48 <= @ < 52 (1)

48 ~ 51을 4구간으로 나눔
(0,1,2,3) 1구간 1짜리
50 <= @ < 51 에 속함 (2)

위치는 (3) - (1) - (2)에 속함

1번 3의 경우 2^(n)-1, 2^(n)-1 중 -> 행 : 2^2 ~ 2^3 -1 열 : 2^2 ~ 2^3 -1
2번 1의 경우 

(0,1,2,3)
1번의 경우 n = 3 인데 이러면 총 개수 64
64 / 4 : 16
16 * 3 + 4 * 0 + 1 * 2 = > 50

5행 4열

n이 주어졌을 때

범위가 
(0~2^(n-1)-1, 0~2^(n-1)-1)                에 속하면 0
(0~2^(n-1)-1, (2^(n-1)~2^(n)-1))        에 속하면 1
((2^(n-1)~2^(n)-1), 0~2^(n-1)-1)        에 속하면 2
((2^(n-1)~2^(n)-1),(2^(n-1)~2^(n)-1)) 에 속하면 3

arr.append() -> 0인지, 1인지, 2인지, 3인지

만약 좀 전처럼 n = 3, r = 5, c = 4로 입력이 들어올 경우
n = 3
첫 비교 (5,4)는
(4~7, 4~7)에 속하기 때문에 arr.append(3)

n = 2 범위 (4~7, 4~7)에서 4개의 사분면으로 나눠서
다음 비교
(4~5,4~5)에 속하기 때문에 arr.append(0)

n = 1 범위 (4~5, 4~5)에서 4개의 사분면으로 나눠서
다음 비교
(5, 4)에 속하기 때문에 arr.append(2)

원하는 값을 찾음, 그렇다면 안에 들어갈 값은
현재 arr = [3,0,2]

arr은 deque

first : (2**n)**2 // 4 = 16 -> 16 * arr.popleft()
second : 16 // 4 -> 4 * arr.popleft()
third(last) : 4 // 4 -> 1 * arr.popleft()

sum_value = first + second + third
-> 16 * 3 + 4 * 0 + 1 * 2 = 50

따라서 50번 째 방문
'''
'''
예시 ) 2, 3, 1 입력이 들어옴
알아야 하는 것, 현재의 첫 위치 (첫 함수라면 0,0, 2번째라면 0,2)

처음으로 선택되는 사분면 1 (arr 배열에 들어갈 값)
배열에 들어가는 값에 따라서 현 위치가 움직여야 함. (cur_r, cur_c) 값을 함수한테 넘겨줌
'''
from collections import deque
import sys

n, r, c = map(int, sys.stdin.readline().split())
arr = deque()

def check(n, r, c, cur_r, cur_c):
    size = 2 ** (n-1)
    if r < cur_r + size and c < cur_c + size:
        return 0
    elif r < cur_r + size and c >= cur_c + size:
        return 1
    elif r >= cur_r + size and c < cur_c + size:
        return 2
    else:
        return 3

cur_x = 0
cur_y = 0

for i in range(n, 0, -1):
    temp = check(i, r, c, cur_x, cur_y)
    arr.append(temp)
    size = 2 ** (i-1)
    if temp == 1:
        cur_y += size
    elif temp == 2:
        cur_x += size
    elif temp == 3:
        cur_x += size
        cur_y += size

result = 0
size = (2 ** n) * (2 ** n) // 4
for _ in range(n):
    result += size * arr.popleft()
    size //= 4

print(result)