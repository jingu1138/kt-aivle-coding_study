# 오예~

import sys

input = sys.stdin.readline

n = int(input())
m = list(map(int, input().split()))
w = list(map(int, input().split()))

m_s = [] # 작은 키 선호 남자
w_s = [] # 작은 키 선호 여자
m_b = [] # 큰 키 선호 남자
w_b = [] # 큰 키 선호 여자

# 남자
for q in range(len(m)):
    if m[q] < 0:
        m_s.append(m[q])

    else:
        m_b.append(m[q])


# 여자
for y in range(len(w)):
    if w[y] < 0:
        w_s.append(w[y])

    else:
        w_b.append(w[y])


m_b.sort()
w_b.sort()
m_s.sort()
w_s.sort()

i = 0 # 여자 인덱스
j = len(m_b) - 1 # 남자 인덱스
cnt = 0 # 커플 성사 횟수

while i != len(w_s):
    if len(w_s) != 0 and len(m_b) != 0: # 리스트에 값이 있을때만 돌게 하기
        if (w_s[i] * -1) > m_b[j]: 
            cnt += 1
            i += 1
            j -= 1

        else:
            j -= 1

        if j < 0:
            break

    else:
        break

i = 0
j = len(m_s) - 1

while i != len(w_b):
    if len(w_b) != 0 and len(m_s) != 0:
        if w_b[i] < (m_s[j] * -1):
            cnt += 1
            i += 1
            j -= 1

        else:
            j -= 1

        if j < 0:
            break

    else:
        break

print(cnt)
