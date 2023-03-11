

## 이동하는 최소 칸 수 구하기
## 1 이동, 0은 이동 못함
## 시작은 (1,1), 타겟은 (n,m)
## bfs로 풀어보자

from collections import deque
import sys
## dfs 구현

## 미로에서는 0으로는 이동할 수 없다.
## 좌우상하 dx로 정의해서 이동시키는 dfs를 살펴보자.

def dfs(maze, x, y, visited, cnt):
    
    ## 상하좌우 이동 좌표
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]

    ## 이동한 위치 표현
    for i in range(4):
        x_nxt = x + dx[i]
        y_nxt = y + dy[i]
    
    ## 이동한 좌표가 visited에 없고, n * m 크기 미로 내 범위 있어야 하며 0으로는 이동하면 안된다.
    
    if 0<= x_nxt <=n and 0 <=y_nxt <=m and not (x_nxt,y_nxt) not in visited and maze[x_nxt][y_nxt]!=0:
                visited.append((x_nxt,y_nxt))
                cnt +=1
                x, y = x_nxt, y_nxt
    for i in range(maze[(x)])       

 

m, n = map(int, sys.stdin.readline().split())
## 미로 입력받기
## 미로 정보는 m개의 정수가 n줄로 붙어서 주어짐
## 리스트로 받은 다음 각각 분리해서 maze 행렬에 넣자

maze = []

for _ in range(n):
    maze.append(list(sys.stdin.readline().strip()))
    
## 방문 상태를 빈 리스트로 만들고 이동한 위치를 넣자

visited = []
    
