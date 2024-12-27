'''
도현이는 바구니를 총 N개 가지고 있고, 
각각의 바구니에는 1번부터 N번까지 번호가 매겨져 있다. 
또, 1번부터 N번까지 번호가 적혀있는 공을 매우 많이 가지고 있다. 
가장 처음 바구니에는 공이 들어있지 않으며, 바구니에는 공을 1개만 넣을 수 있다.

도현이는 앞으로 M번 공을 넣으려고 한다.
 도현이는 한 번 공을 넣을 때, 공을 넣을 바구니 범위를 정하고, 
 정한 바구니에 모두 같은 번호가 적혀있는 공을 넣는다. 
 만약, 바구니에 공이 이미 있는 경우에는 들어있는 공을 빼고, 새로 공을 넣는다. 
 공을 넣을 바구니는 연속되어 있어야 한다.

공을 어떻게 넣을지가 주어졌을 때, M번 공을 넣은 이후에 
각 바구니에 어떤 공이 들어 있는지 구하는 프로그램을 작성하시오.
'''

'''
n개 바구니, 1~n번까지 번호가 적혀있는 공을 매우 많이 가지고 있음.
가장 처음 바구니에는 공이 들어있지 않음. 바구니에는 공을 1개만 넣을 수 있음

m번 공을 넣으려 함.
한 번 공을 넣을 때 공을 넣을 바구니 범위를 정하고
정한 바구니에 모두 같은 번호가 적혀있는 공을 넣음.
바구니에 공이 이미 있는 경우 들어 있는 공을 빼고 새로 공을 넣음
공을 넣을 바구니는 연속되어 있어야ㅕ 함.
5 4 (n, m)
1 2 3 i번 바구니부터 j번 바구니까지 k번 번호가 적혀져 있는 공을 넣는다
3 4 4
1 4 1
2 2 2

0 0 0 0 0
3 3 0 0 0
    4 4
1 1 1 1 0
  2
1 2 1 1 0

예시 출력
1 2 1 1 0

1~n번 
'''
import sys
n, m = map(int, input().split())
arr = [0]*(n+1)
for i in range(m):
    x,y,z = map(int, sys.stdin.readline().split())
    for j in range(x,y+1):
        arr[j] = z

print(*arr[1:])