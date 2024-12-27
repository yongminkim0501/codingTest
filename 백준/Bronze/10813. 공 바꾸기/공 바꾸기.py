# 공 바꾸기
# 바구니를 총 n개 가지고 있음.
# 각각 바구니에는 1~n번까지 번호가 매겨져 있음
# 바구니에는 공이 1개씩 들어있고, 처음에는 바구니에 적혀있는 번호와 같은 번호 적힌 공 들어잇음.
# m번 공을 바꾸려 함.
# 공을 바꿀 바구니 2개 선택하고, 두 바구니에 들어있는 공을 서로 교환
import sys
def change(x,y):
    tmp = x
    x = y
    y = tmp
    return x, y

n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(i+1)
for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    arr[x-1], arr[y-1] = change(arr[x-1], arr[y-1])
print(*arr)

'''
1 2 3 4 5
2 1 3 4 5
2 1 4 3 5
3 1 4 2 5

'''