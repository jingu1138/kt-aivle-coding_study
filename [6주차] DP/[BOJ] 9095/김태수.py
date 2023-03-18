t=int(input())
dp = [0] * 12

num = []
for i in range(t):
    n = int(input())
    num.append(n)

    
dp[1] = 1
dp[2] = 2

for i in range(3, 12):
    dp[i] = (dp[i-2] * 3) + 1
  
for i in range(len(num)):
    print(dp[num[i]])
