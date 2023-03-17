from collections import deque

n, m = map(int, input().split())

graph = []
    
for i in range(n):
    graph.append(list(map(int, input())))

#visited = [[False] * n for _ in range(m)]
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a, b):
    queue = deque()
    queue.append((a,b))
    while queue:
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            
            if x<0 or x>=n or y<0 or y>=m:
                continue
            if graph[x][y]==0:
                continue
            
            if graph[x][y]==1:
                graph[x][y] = graph[a][b]+1
                queue.append((x, y))
    return graph[n-1][m-1]


print(bfs(0.0))
