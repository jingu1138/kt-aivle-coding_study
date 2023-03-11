from collections import deque

## dfs 구현
def dfs(graph, a, visited):
    # 방문한 노드 표시
    visited[a] = True
    print(a, end = ' ')
    # 다음 노드 방문 안했으면 dfs
    for i in graph[a]:
        if not visited[i]:
            dfs(graph, i, visited)

## bfs 구현
def bfs(graph, start, visited):
    queue = deque([start])
    # 방문 노드 표시
    visited[start] = True
    
    while queue:
        a = queue.popleft()
        print(a, end=' ')
    ## graph에서 방문하지 않은 노드 있으면 queue에 넣기
        for i in graph[a]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
     
## 노드 연결 상태 
## graph는 n개 정점에 대한 간선 연결 정보

graph = [[] for i in range(n+1)]
n, m, v = map(int,input().split())
for i in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(n):
    graph[i].sort()
    
visited = [False]*n

print(dfs(graph,v,visited))
print(bfs(graph,v,visited))

