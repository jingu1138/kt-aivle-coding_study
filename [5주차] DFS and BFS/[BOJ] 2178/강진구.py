import sys

n,m = map(int, sys.stdin.readline().split())

graph = []
visited = [[False]*m for _ in range(n)]


for _ in range(n):
    graph.append(list(sys.stdin.readline().strip()))
    
cnt = 0
def dfs(graph, visited, v):
    y,x = v
    d_x = [1,-1,0,0]
    d_y = [0,0,1,-1]
    for i in range(4):
        dx = x + d_x[i]
        dy = y + d_y[i]
        if graph[dy][dx] == 1 and visited[dy][dx]==False:
            visited[dy][dx] = True
            cnt+=1
            dfs(graph, visited, (dy,dx))

dfs(graph,visited,(0,0))
print(cnt)
