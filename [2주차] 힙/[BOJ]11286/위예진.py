# N: 연산의 개수, x_list: 연산에 대한 정보 리스트
import sys
import heapq
input = sys.stdin.readline

N = int(input())
positive = []
negative = []

for _ in range(N):
    x = int(input())
    if x == 0:
        if positive and negative:
            if positive[0] >= negative[0]:
                print(-heapq.heappop(negative))
            else:
                print(heapq.heappop(positive))
        elif positive and not negative:
            print(heapq.heappop(positive))
        elif negative and not positive:
            print(-heapq.heappop(negative))    
        else:
            print(0)
    elif x > 0:
        heapq.heappush(positive, x)
    else:
        heapq.heappush(negative, -x)