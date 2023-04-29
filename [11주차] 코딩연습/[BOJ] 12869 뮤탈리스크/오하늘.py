# 뮤탈리스크
import sys
input = sys.stdin.readline

n = int(input()) # SCV 수
scv_h = list(map(int, input().split())) # 각 SCV의 체력

dp = [[0 for i in range(61) for j in range(61)] for k in range(61)] # 3차원 리스트 생성

# 나의 생각
# 탑 다운 형식으로 메모이 제이션을 이용
# 
# def dfs():
    # i j k 가 0보다 작고, 최소 값인 경우 내보냄
    # return answer
    
    # 이미 방문한 dp면 이거 출력
    
    # 방문 안했으면 1, 3, 9 조합으로 dfs
    
# print (i,k,j ~)
