# 시간초과

import sys

input = sys.stdin.readline

n = int(input())
m = list(map(int, input().split()))
w = list(map(int, input().split()))

m_s = []
w_s = []

# 작은 키 원하는 남자
for q in range(len(m)):
    if m[q] < 0:
        m_s.append(m[q])
        m[q] = 0
    
        
        
# 작은 키 원하는 여자
for y in range(len(w)):
    if w[y] < 0:
        w_s.append(w[y])
        w[y] = 0
        
        
m.sort()
w.sort()
m_s.sort()
w_s.sort()

cnt = 0

# 큰 키 원하는 남자 짝 찾기
for i in range(len(m)):
    for j in range(len(w_s)):
        if m[i] != 0 and m[i] < (w_s[j] * -1):
            cnt += 1
            w_s[j] = 0
            
# 작은 키 원하는 남자 짝 찾기
for a in range(len(m_s)):
    for b in range(len(w)):
        if w[b] != 0 and (m_s[a] * -1) > w[b]:
            cnt += 1
            w[b] = 0

print(cnt)
