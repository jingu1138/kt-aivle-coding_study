
## 9 3 1 순으로 체력 감소
## 가장 체력 높은 순부터 쳐야함



## 입력받기
scv =  int(input())
scv_hp = list(map(int,input().split()))

dp = [[[0 for _ in range(61)] for _ in range(61)] for _ in range(61)]

### 각 scv에 -9 -3 -1 하는 dfs?



## scv 3마리인 기준으로 통합

while len(scv) < 3:
    scv.append(0) 

def dfs(x, y, z):
    if x == 0 and y ==0 and z ==0 :
        return 0
    if dp[x][y][z]:
        return dp[x][y][z]
    
    ## 체력 빼도 0 밑으로 떨어지면 0으로 바꾼다
    
    dp[x][y][z] = 1+ min(dfs(max(x-9,0), max(y-3,0), max(z-1,0)), dfs(max(x-9,0), max(y-1,0), max(z-3,0)), dfs(max(x-3,0), max(y-9,0), max(z-1,0)),
    dfs(max(x-3,0), max(y-1,0), max(z-9,0)), dfs(max(x-1,0), max(y-3,0), max(z-9,0)), dfs(max(x-1,0), max(y-9,0), max(z-3,0)))
    
    return dp[x][y][z]

print(dfs([scv_hp[0], scv_hp[1], scv_hp[2]]))
