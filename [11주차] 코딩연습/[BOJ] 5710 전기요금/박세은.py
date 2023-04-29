lst = []
pay = [2, 2,
       3, 3,
       5, 5,
       7, 7, 7, 7, 7]  # 자릿수별 요금

while True:  # 입력받기
    a, b = map(int, input().split())

    if a == 0 and b == 0:
        break

    lst.append((a, b))

n = 0  # 총 전기 사용량

# 총 전기 사용량 구하기
for i in lst:
    pnum = len(str(i[0])) - 1  # a 자릿수 구하기

    if len(str((i[0] - 1))) != pnum:
        pnum -= 1

    if 1 < pnum < 4:
        n = (i[0] + 100) // 3

    elif 3 < pnum < 6:
        n = (i[0] + 20300) // 5

    else:
        n =
