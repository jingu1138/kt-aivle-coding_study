import sys

input = sys.stdin.readline

n = int(input())

dp = [0]*(n+1)
schedule = []

for _ in range(n):
    schedule.append(tuple(map(int,input().split())))

print(schedule)
for i in range(1,n+1):
    max_v = 0
    sum_m = 0
    for idx,t in enumerate(schedule[:i]):
        if idx+t[0] == i:
            sum_m += max(t[1],max_v)
            print(sum_m,i)
        
