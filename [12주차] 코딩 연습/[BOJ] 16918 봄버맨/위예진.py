# 폭탄이 있는 칸은 3초 뒤 폭발 -> 폭탄 있던 칸, 인접 네 칸이 빈 칸이 됨 (인접 네 칸에 폭탄 있더라도 폭발 X)
# 0. 일부 칸에 폭탄 설치 -> 1. 1초 지남 -> 2. 폭탄 설치 되지 않았던 모든 칸에 폭탄 설치
#   -> 3. 0.의 폭탄이 모두 터짐 -> 4. 빈 칸에 폭탄 설치됨 -> 5. 3.의 폭탄이 모두 터짐 -> 6. 빈 칸에 폭탄 설치됨
# 빈 칸은 '.'로, 폭탄은 'O'

# 폭탄이 저장됐던 시간들과 장소들을 저장해야 하나,,,,?
# 시간마다의 그래프를 저장해야 하나...?

import sys
input = sys.stdin.readline

rows, cols, target = map(int, input().split())    # 격자판의 행, 열의 수, 알고자 하는 시간(초)
bomb = []    # 격자판 리스트
for _ in range(rows):
    tmp = list(input().rstrip())
    
    for  i, b in enumerate(tmp):
        if b == 'O':    # 폭탄이 설치돼 있다면, 
            tmp[i] = 3    # 폭발 시간 설정
        else:
            tmp[i] = False
            
    bomb.append(tmp)
    
# 상하좌우 이동
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for t in range(2, target + 1):    # 목표 시간까지 반복
    # 시간 초가 짝수 -> 빈 칸에 폭탄 설치, 홀수 -> 폭탄 터짐
    
    if t % 2:    # 시간 초가 홀수,
        # 폭탄 터트리기 (터진 폭탄 위치, 주위 빈 칸으로 변경)
        for r in range(rows):
            for c in range(cols):
                if bomb[r][c] and bomb[r][c] <= t:    # 해당 시간에 터질 폭탄 이라면, 
                    bomb[r][c] = False    # 해당 폭탄 터트리고, 빈 칸으로 변경
                    for mr, mc in zip(dr, dc):    # 상하좌우 확인
                        mover, movec = r + mr, c + mc
                        if 0 <= mover < rows and 0 <= movec < cols:    # 범위를 넘지 않고,
                            if not bomb[mover][movec] or bomb[mover][movec] > t:    # 터질 폭탄이 있는 곳이 아니라면,
                                bomb[mover][movec] = False
    else:    # 시간 초가 짝수,
        # 빈 칸에 폭탄 설치
        for r in range(rows):
            for c in range(cols):
                if not bomb[r][c]:    # 폭탄이 없다면,
                    bomb[r][c] = t + 3    # 폭탄 설치 (터지는 시간 설정)

# 출력 모양으로 바꿔서 출력
for r in range(rows):
    for c in range(cols):
        if bomb[r][c]:    # 폭탄이 있다면,
            bomb[r][c] = 'O'
        else:
            bomb[r][c] = '.'
    print(''.join(bomb[r]))