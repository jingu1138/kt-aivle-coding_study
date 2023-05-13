import sys
input = sys.stdin.readline

n = int(input())

# 그래프 생성
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0

def dfs(x, y, h):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i] 
        
        if nx >=n or ny >=n or nx<0 or ny<0:
            continue
        if not visited[nx][ny] and graph[nx][ny] > h:
            dfs(nx, ny, h)
            
for h in range(101):
    count = 0
    visited = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] > h and not visited[i][j]:
                dfs(i, j, h)
                count = count + 1
        cnt = max(cnt, count)
        
print(cnt)
