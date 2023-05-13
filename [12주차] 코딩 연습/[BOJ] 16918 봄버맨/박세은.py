r, c, n = map(int, input().split())

grp = []

# 격자판 입력
for _ in range(r):
    grp.append(input())


# 격자판위 폭탄 좌표
def bomb_f(r, c, grp):
    bomb = []
    for b in range(r):
        for i in range(c):
            if grp[b][i] == "O":
                bomb.append([b, i])

            else:
                continue

    return bomb


j = 0  # 초

while j <= n:  # j초가 n초보다 커지면 반복문 탈출
    lst = bomb_f(r, c, grp)  # 현재 격자판위 폭탄좌표 저장
    full = [list("O" * c) for _ in range(r)]  # 모두 폭탄으로 찬 격자판 생성
    j += 1  # 1초 +

    if j % 2 != 0 and j != 1:  # 1초가 아닌 홀수초일때만 실행
        for q in lst:
            full[q[0]][q[1]] = "."  # 폭탄 위치 비워주기

            if q[0] < r - 1:
                full[q[0] + 1][q[1]] = "."  # 상

            if 0 < q[0]:
                full[q[0] - 1][q[1]] = "."  # 하

            if q[1] < c - 1:
                full[q[0]][q[1] + 1] = "."  # 우

            if 0 < q[1]:
                full[q[0]][q[1] - 1] = "."  # 좌

        grp = full

    else:
        continue

full = [list("O" * c) for _ in range(r)]  # full 격자판 초기화

if n % 2 == 0:  # 짝수초일때 full 격자판 출력
    for i in range(r):
        print("".join(full[i]))

else:  # 홀수초일때 grp 격자판 출력
    for i in range(r):
        print("".join(grp[i]))
