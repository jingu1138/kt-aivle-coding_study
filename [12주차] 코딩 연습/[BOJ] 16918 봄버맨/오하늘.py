#봄버맨
import sys
input = sys.stdin.readline

R, C, N = map(int, input().split())
graph = [list(map(str,input().strip())) for i in range(R)] #count 0

cnt = 1

# 짝수
if N % 2 == 0:
    g = [list('O'*C) for i in range(R)]
    for i in range(R):
        for j in range(C):
            print(g[i][j], end='')
        print()

else:
    while cnt <= N :
    # 폭발 (1을 제외한 홀수)
        if cnt%2==1 and cnt !=1 :
            visited = [[False]*C for i in range(R)] # 방문 초기화
            # 하, 상, 오, 왼
            for i in range(R):
                for j in range(C):
                    if graph[i][j] == 'O':
                        if graph[i][j] :
                            graph[i][j] = '.'
                            visited[i][j] = True
                        #하
                        if i+1 < R:
                            if graph[i+1][j] == 'O' and visited[i+1][j]==False: continue
                            graph[i+1][j] = '.'
                            visited[i+1][j] = True
                        #상
                        if i-1 >= 0: 
                            if graph[i-1][j] == 'O' and visited[i-1][j]==False: continue
                            graph[i-1][j] = '.'
                            visited[i-1][j] = True
                        #오
                        if j+1 < C : 
                            if graph[i][j+1] == 'O' and visited[i][j+1]==False: continue
                            graph[i][j+1] = '.'
                            visited[i][j+1] = True
                        #왼
                        if j-1>= 0 :
                            if graph[i][j-1] == 'O' and visited[i][j-1]==False: continue
                            graph[i][j-1] = '.'
                            visited[i][j-1] = True
                    else :
                        if visited[i][j] == False:
                            graph[i][j] = 'O'
                            visited[i][j] = True
        cnt += 2
                
    for i in range(R):
        for j in range(C):
            print(graph[i][j], end='')
        print()
