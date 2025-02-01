'''
도시 n개 (연결이 되어 있을수도, 안될 수도 있음)
여행 일정이 주어질 때, 이 여행 경로가 가능한 것인지 알아보자

예를 들어 도시가 5개, A-B, B-C, A-D, B-D, E-A
ECBCD => E - A - B - C - B - C - B - D 
라는 여행경로를 통해 목적을 달성할 수 있음

첫 줄에 도시의 수 n이 주어짐
둘째 줄에 여행 계획에 속한 도시들의 수 m이 주어짐
i번째 줄의 j번째 수는 i번 도시와 j번 도시의 연결 정보를 의미
1이면 연결된 것, 0이면 연결이 되지 않은 것

a와 b가 연결되었으면 b와 a도 연결, 마지막 줄에는 여행 계획이 주어짐

예제 입력
3
3
0 1 0 # 1번째 줄의 2번째 수 => 1번과 2번이 연결되어 있음을 나타냄, 
        나머지는 연결되어있지 않음을 나타냄
1 0 1 
0 1 0
1 2 3 # 마지막 줄에는 여행 계획이 주어짐 => 1 -> 2 -> 3 으로 가는 것을 의미함


1 - 2
2 - 1  3
3 - 2

1 -> 2 -> 3

yes 출력
'''
import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

arr = [i for i in range(n+1)]

def find(x):
    if arr[x] != x:
        arr[x] = find(arr[x])
    return arr[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a < b:
        arr[b] = a
    else:
        arr[a] = b

for i in range(1, n+1):
    tmp = list(map(int, sys.stdin.readline().split()))
    for j in range(1, n+1):
        if tmp[j-1] == 1:
            union(i,j)

result = list(map(int, sys.stdin.readline().split()))
compare = find(result[0])
flag = True

for i in result:
    if find(i) != compare:
        flag = False
        break

if flag == False:
    print("NO")
else:
    print("YES")