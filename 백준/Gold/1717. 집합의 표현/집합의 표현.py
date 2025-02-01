'''
초기에 n+1 개의 집합 {0},{1},{2}, ... ,{n}
여기에 합집합 연산과 두 원소가 같은 집합에 포함되어 있는지를
확인하는 연산을 수행하려고 한다.
집합을 표현하는 프로그램을 작성

input 
첫째 줄에 n, m이 주어짐
m은 입력으로 주어지는 연산의 개수
다음 m개의 줄에는 각각의 연산이 주어짐

합집합은 0 a b의 형태로 입력이 주어짐

이는 a가 포함되어 있는 집합과 b가 포함되어 있는 집합을 합침
1 a b 형태로 입력
a b 같은 집합에 포함되어 있는지를 확인


7 8
0 1 3 (합집합)
1 1 7 (a가 포함되어 있는 집합과 b가 포함되어 있는 집합을 합침 
       => 1이 포함되어 있는 집합과, 7이 포함되어 있는 집합)
0 7 6 (합집합 => 7이 포함되어 있는 집합과 7이 포함되어 있는 집합)
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
'''

'''
유니온 파인드
그래프 알고리즘, 두 노드가 같은 그래프에 속하는 지 판별하는 알고리즘
노드를 합치는 union연산과 노드의 루트 노드를 찾는 find연산으로 이루어짐
'''
import sys
sys.setrecursionlimit(10**5)
arr = []

def find(x):
    if arr[x] != x:
        arr[x] = find(arr[x])
    return arr[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a<b:
        arr[b] = a
    else:
        arr[a] = b

n, m = map(int, sys.stdin.readline().split())

for i in range (n+1):
    arr.append(i)

for _ in range(m):
    a,b,c = map(int, sys.stdin.readline().split())

    if a == 0:
        union(b,c)
    else :
        if find(b) == find(c) :
            sys.stdout.write("YES\n")
        else:
            sys.stdout.write("NO\n")