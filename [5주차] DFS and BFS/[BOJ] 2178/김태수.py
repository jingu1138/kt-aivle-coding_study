from collections import deque

x=0
y=0

n, m = map(int, input().split())

visited = [[False] * n for _ in range(m)]

graph = []

for i in range(n):
    graph.append(list(map(int, input())))
    
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


def bfs(a, b):
    cnt = 1
    for i in range(4):
        x = a + dx[i]
        y = b + dy[i] 
        if graph[x][y] ==1:
            cnt += cnt
        if x>m or y>n or x<0 or y<0:
            i = 0
    print(cnt)        
            
bfs(0,0)
