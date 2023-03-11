import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())

graph = []
visited = [[False]*m for _ in range(n)]


for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().strip())))
    
cnt = 1

def bfs(grahp, visited):
    que = deque([(0,0,0)])
    visited[0][0] = True
    
    while que:
        r,c,cnt = que.popleft()
        if r==n-1 and c==m-1:
            return cnt
    
        dc = [1,-1,0,0]
        dr = [0,0,1,-1]
        for i in range(len(dc)):
            nc = c + dc[i]
            nr = r + dr[i]
            print(nr, nc)
            if (0<=nc<m) and (0<=nr<n) and (grahp[nr][nc]==1) and (visited[nr][nc]==False):
                cnt += 1
                que.append((nr,nc,cnt))
                visited[nr][nc]=True
                

print(bfs(graph, visited))

