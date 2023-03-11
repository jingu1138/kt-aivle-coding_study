# 미로 탐색
import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # n개의 줄 m개의 정수
arr = [list(map(int, input().split())) for _ in range(N)]

visited = [[False]*M]*N

def dfs(arr, i, j, visited):
    visited[i][j] = True # 방문했음
    for k in arr[i][]:
        if not visited[i][k] and arr[i][k] == 1:
            dfs(arr, i, k, visited)
            
dfs(arr, 0, 0, visited)
