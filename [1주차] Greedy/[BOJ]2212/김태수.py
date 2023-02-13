N = int(input())
K = int(input())
num = list(map(int, input().split()))
gap = []

num.sort()
total = max(num) - min(num)
for i in range(1, N):
    gap.append(num[i]-num[i-1])

gap.sort(reverse = True)

sum = 0
for i in range(0, K-1):
    sum += gap[i]

answer = total - sum
print(answer)
