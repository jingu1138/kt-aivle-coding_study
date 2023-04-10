# 나는 멍청이~

import sys
from collections import defaultdict, deque

input = sys.stdin.readline

n = int(input())

a,b = map(int, input().split())

m = int(input())
graph = defaultdict(list)

for _ in range(m):
    k,v = map(int, input().split())
    graph[k].append(v)

visited = [False]*n
cnt = 0
que = deque([(a,b,cnt)])

while que:
    st,ed,cnt = que.popleft()
    visited[st] = True
    
    
