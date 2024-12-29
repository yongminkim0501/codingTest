'''
어떤 배추에 지렁이가 한 마리라도 살고 있으면, 이 지렁이는 인접 배추로 이동 가능
따라서 걔도 보호받을 수 있음.
상하좌우 네 방향에 다른 배추가 위치한 경우에 인접
필요한 지렁이가 몇 개인지
'''
import sys
t = int(input())
sys.setrecursionlimit(10**5)
# 테스트 케이스 첫째 줄에는 배추를 심은 배추 밭은 
# 가로 m, 세로 n, 배추가 심어져 있는 위치의 개수 k
# 다음 k줄에는 배추의 위치 x,y 가 주어짐.
# 두 배추의 위치가 같은 경우 없음
move_i = [0,0,1,-1]
move_j = [-1,1,0,0]
count = 0

result = []
for i in range(t):
    m, n, k = map(int, input().split())
    
    '''arr = [[] for _ in range(n+1)]
'''
    arr = [[0 for _ in range(m+1)] for i in range(n+1)]
    '''for i in range(m):
        for j in range(n):
            arr[j].append(0)
    print(arr)'''
    def dfs(ti,tj):
        global count
        if ti > n or ti < 0 or tj > m or tj < 0:
            return False
        else:
            if arr[ti][tj] == 1:
                arr[ti][tj] = 0
                for z in range(4):
                    tmp_i = ti + move_i[z]
                    tmp_j = tj + move_j[z]
                    count += 1
                    dfs(tmp_i,tmp_j)
                return True

    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        arr[y][x] = 1

    for j in range(n):
        for l in range(m):
            if arr[j][l] == 1:
                dfs(j,l)
                result.append(count)
        count = 0
    print(len(result))
    result = []