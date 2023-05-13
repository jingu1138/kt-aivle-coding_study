# 어떤 지역의 높이 정보를 파악 -> 그 지역에 많은 비가 내렸을 때 물에 잠기지 않는 안전한 영역이 최대로 몇 개가 만들어 지는지
# 장마철에 내리는 비의 양에 따라 일정한 높이 이하의 모든 지점은 물에 잠긴다고 가정

# 물에 잠기려면 우선 최소 높이부터 시작 -> 최대 높이까지 확인


import sys
input = sys.stdin.readline

# 안전한 지역인지 구분하는 함수
def is_safe(hmap, water, visited):    # dfs,,,
    # hmap: 지역 높이 리스트, water: 침수된 지역인지, visited: 안전한 지역인지 확인한 곳인지
    
    # 상하좌우 연결된 모든 안전한 지역 탐색
    
    
    return True

# 잠기는 지점 표시
def do_water(hmap, water, n, height):
    # hmap: 지역 높이 리스트, water: 침수된 지역인지, n: hmap의 너비, height: 침수 기준 높이
    
    for r in range(n):
        for c in range(n):
            if hmap[r][c] <= height:
                water[r][c] = True
    
    return water

n = int(input())
min_h, max_h = int(1e3), 0    # 최소, 최대 높이
hmap = []    # 높이 정보 리스트
for _ in range(n):
    tmp = list(map(int, input().split()))
    hmap.append(tmp)
    min_h, max_h = min(min_h, min(tmp)), max(max_h, max(tmp))
print(min_h, max_h)

water = [[False] * n for _ in range(n)]    # 잠긴 지점인지 표시하는 리스트 초기화
visited = [[False] * n for _ in range(n)]    # 안전 지역인지 순회할 때, 방문한 적 있는지 확인하는 리스트
print(water)

for height in range(min_h, max_h):
    
    # h 이하인 지역은 잠긴 지점 표시
    water = do_water(hmap, water, n, height)
    