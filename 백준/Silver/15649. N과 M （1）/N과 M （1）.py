'''
백트래킹 문제

자연수 n, m이 주어질 떄, 아래 조건을 만족하는 길이가 m인 수열을 모두 구하는 프로그램을 작성
1부터 n까지 자연수 중에서 중복 없이 m개를 고른 수열

예제 입력
3 1
1
2
3

예제 입력
4 2
1 2, 3 1
1 3, 3 2
1 4, 3 4
2 1, 4 1
2 3, 4 2
2 4, 4 3

백트래킹은 보통 해를 찾는 도중 막히면, 되돌아가서 다시 해를 찾는 기법

재귀적 탐색과 되돌리기 활용
'''
n, m = map(int, input().split())
visit = [False] * (n+1)
s = []
def dfs():
    if len(s) == m :
        for i in s:
            if i != s[-1]:
                print(i, end = " ")
            else:
                print(i)
        return
    
    for i in range(1, n+1):
        
        if visit[i]:
            continue

        visit[i] = True
        s.append(i)
        
        dfs()
        
        s.pop()
        visit[i] = False
dfs()