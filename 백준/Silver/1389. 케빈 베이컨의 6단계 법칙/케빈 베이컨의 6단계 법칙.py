import sys
from collections import deque
'''def bfs(graph, start, n):
    visited = [0 for _ in range (n+1)]
    queue = deque([start])
    visited[start] = 1
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[v]+1

    return sum(visited) - n'''

def bfs(graph, start, n):
    visited = [0] * (n + 1)
    queue = deque([start])
    visited[start] = 1

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if visited[neighbor] == 0:
                visited[neighbor] = visited[node] + 1
                queue.append(neighbor)

    return sum(visited) - n

def main():
    n, m = map(int, sys.stdin.readline().split(" "))
    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        a,b = map(int, sys.stdin.readline().split(" "))
        graph[a].append(b)
        graph[b].append(a)

    result = []
    for graph_idx in range(1, n+1):
        temp_data = bfs(graph, graph_idx, n)
        result.append(temp_data)

    for result_idx in range(len(result)):
        if result[result_idx] == min(result):
            print(result_idx+1)
            break
if __name__ == "__main__":
    main()