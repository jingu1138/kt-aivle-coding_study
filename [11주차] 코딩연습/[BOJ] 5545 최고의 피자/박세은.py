n = int(input())  # 토핑 종류 수
a, b = map(int, input().split())  # 도우, 토핑 가격
c = int(input())  # 도우 열량
d = [int(input()) for _ in range(n)]  # 토핑 열량

d.sort(reverse=True)  # 내림차순 정렬

pay = 0  # 피자 가격
cly = c  # 피자 열량
cly_a = 0  # 1원당 피자 열량
ans = c // a  # 1원당 피자 열량 최대값

i = 0

while True:

    if i == n:
        break

    pay = a + (b * (i + 1))
    cly += d[i]
    cly_a = cly // pay
    i += 1

    if cly_a >= ans:
        ans = cly_a

    else:
        break


print(ans)
