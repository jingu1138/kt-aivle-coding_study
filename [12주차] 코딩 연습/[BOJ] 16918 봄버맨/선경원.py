

## R * C 짜리 격자판, 각 칸에는 폭탄 or 빈 공간
## 폭탄은 3초 후 폭발 => 폭탄 칸 + 인접 4칸 빈칸 됨
## 인접 칸에 폭탄 있으면 폭발 없이 폭탄만 사라짐

## 봄버맨 행동
## 일부 칸에 폭탄 설치
## 1초 휴식 (2초 남음)
## 폭탄 없는 칸에 모두 폭탄 설치(기존 폭탄 1초 남음)

## 짝수 시간마다 테이블 모든 칸에 폭탄이 깔린다

## 입력 (초기 폭탄 설치)


## 0s : 초기 상태
## 1s : 가만히
## 2s : 외부 폭탄 설치
## 3s : 초기 폭탄 터짐 
## 4s : 빈 자리 폭탄 채움
## 5s : 2s 때 설치한 폭탄 터짐 = 처음 모양 복귀
## 6s : 외부 폭탄 설치


R, C, N = map(int, input().split())
table = list(list(input().rstrip()) for _ in range(R))
    
## 폭탄별 타이머를 만들자
## 3초가 되면 table에서 0인 놈 찾아서 상하좌우 . 으로 바꿔주기
## 짝수 초에 0인 애들만 +1초씩

## 홀수 초에도 4 주기로 돈다

timer = [[0]*C for _ in range(R)]

neighbors = [(0, -1), (0, 1), (1, 0), (-1, 0)]


## n = 1이면 테이블 유지

if N == 1:  
    
    for i in range(R):
        for j in range(C):
            print(table[i][j], end='')
        print()

## 짝수 초 폭탄 없는 칸에 모두 폭탄 설치

elif N % 2 == 0:
    for i in range(R):
        for j in range(C):
            print('O', end='')
        print()

## 홀수 초는 4마다 주기

## time_board로 터진 결과를 저장해서 내보내자

elif N % 4 == 3:
    
    time_board = [['O'] * C for _ in range(R)] ## 처음 폭탄 터졌을 때 
    
    for i in range(R):
        for j in range(C):
            if table[i][j] == 'O':
                time_board[i][j] = '.'  ## 폭탄 자리는 터져서 . 으로 바꾼다
                
                for k in range(4):
                    ni = i + neighbors[k][0]
                    nj = j + neighbors[k][1]
                    if 0 <= ni < R and 0 <= nj < C:
                        time_board[ni][nj] = '.'  ## 폭탄 상하좌우 . 으로 바꾼다
                        
    for i in range(R):
        for j in range(C):
            print(time_board[i][j], end='')   ## 터진 결과 출력
        print()
        

elif N % 4 == 1:  ## 나중에 설치된 폭탄 폭발
    
    time_board = [['O'] * C for _ in range(R)]  ## time_board 초기화
    for i in range(R):
        for j in range(C):
            if table[i][j] == 'O':
                time_board[i][j] = '.'
                
                for k in range(4):
                    ni = i + neighbors[k][0]
                    nj = j + neighbors[k][1]
                    if 0 <= ni < R and 0 <= nj < C:
                        time_board[ni][nj] = '.'

    time_board_2 = time_board  ## board에 결과 복사
    
    time_board = [['O'] * C for _ in range(R)]  ## time_board는 다시 초기화

    for i in range(R):
        for j in range(C):
            if time_board_2[i][j] == 'O':
                time_board[i][j] = '.'
                
                for k in range(4):
                    ni = i + neighbors[k][0]
                    nj = j + neighbors[k][1]
                    if 0 <= ni < R and 0 <= nj < C:
                        time_board[ni][nj] = '.'

    for i in range(R):
        for j in range(C):
            print(time_board[i][j], end='')
        print()
