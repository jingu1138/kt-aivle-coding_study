import sys
input = sys.stdin.readline

while True:
    A, B = map(int, input().split())
    if (A == 0) and (B == 0):
        break
    
def solution(a, b):
    # 총 전기 사용량 구하기
    if a <= 200:
        watt = a // 2   
    elif (a>200) and (a<=29900):
        watt = 100 + ((a - 200)//3)
    elif (a > 29900) and (a<=4979900):
        watt = 10000 + ((a - 29900)//5)
    else:
        watt = 1000000 + ((a - 4979900)//7)
    
    # 절대값으로 각각의 전기 사용량 구하기
