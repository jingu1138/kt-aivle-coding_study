# DFS와 BFS
import sys
input = sys.stdin.readline

N, M, V= map(int, input().split()) # 정점 개수, 간선 개수, 시작 정점

graph = [[0 for j in range(2)]for i in range(M+1)] # 2차원 리스트 선언 *질문
graph[0] = [0,0]
for i in range(1,M+1):
    l = list(map(int, input().split()))
    graph[i] = l
    print(graph[i])
    
visited = [False] * M # 방문처리 false 처리

def dfs(graph, v, visited): # 깊이 탐색 변수로는 graph, 시작노드, 방문처리
    visited[v] = True # 나 방문했어요
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
            
print(dfs(graph, V, visited))
