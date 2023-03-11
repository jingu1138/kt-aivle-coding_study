import sys
from collections import deque

n, m = map(int, input().split())
gph = [[]]
ans = []

for _ in range(n):
    gph.append(list(map(int,input())))

visited = [False] * (n * m)

def bfs(gph, start, visited):
    que = deque([start])
    visited[start] = True
    
    while que :
        
        a = que.popleft()
        ans.append(a)
        
        for i in gph[a]:
            if not visited[i]:
                que.append(i)
                visited[i] = True
