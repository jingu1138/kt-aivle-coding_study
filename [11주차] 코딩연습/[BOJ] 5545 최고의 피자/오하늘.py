# 최고의 피자
import sys
input = sys.stdin.readline

n = int(input()) #토핑의 종류 수
a, b = map(int, input().split()) # 도우의 가격, 토핑의 가격
c = int(input()) # 도우의 열량

t_info = []
for i in range(n):
    t = int(input())
    t_info.append(t) # 토핑의 열량
t_info.sort(reverse=True) # 내림차순 정렬
    
max_k = c//a # 토핑 0

# 최대 찾기
for i in range(n):
    c = c+t_info[i]
    a = a+b
    if max_k <= c//a: #이번 값이 더 크면
        max_k = c//a # 최고의 피자 갱신
    else : break

print(int(max_k))
