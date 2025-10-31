'''
방향 없는 그래프가 주어졌을 때, 연결 요소의 개수를 구하는 프로그램을 작성하시오

연결 요소의 개수?

'''
import sys

from collections import deque


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

def main():
    n, m = map(int, sys.stdin.readline().split(" "))
    graph = [[] for _ in range (n+1)]
    for _ in range (m):
        u,v = map(int, sys.stdin.readline().split(" "))

        graph[u].append(v)
        graph[v].append(u)
    '''
    graph = [
        [],  # 인덱스 0 (사용 안 함)
        [2, 5],  # 노드 1 → 2, 5와 연결
        [1, 5],  # 노드 2 → 1, 5와 연결
        [4],  # 노드 3 → 4와 연결
        [3, 6],  # 노드 4 → 3, 6과 연결
        [1, 2],  # 노드 5 → 1, 2와 연결
        [4]  # 노드 6 → 4와 연결
    ]'''
    visited = [False for i in range(len(graph)+1)]
    visited[0] = True
    tree_count = 0
    for graph_idx in range (1, len(graph)):
        if not visited[graph_idx]:
            bfs(graph, graph_idx, visited)
            tree_count+=1

    print(tree_count)

if __name__ == "__main__":
    main()
