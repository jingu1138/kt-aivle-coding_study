# 런타임 에러

import sys

input = sys.stdin.readline

n = int(input())
m = list(map(int, input().split()))
w = list(map(int, input().split()))

m_s = []
w_s = []
m_b = []
w_b = []

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

i = 0
j = len(m_b) - 1
cnt = 0

while i != len(w_s):
    if (w_s[i] * -1) > m_b[j]:
        cnt += 1
        i += 1
        j -= 1

    else:
        j -= 1

    if j < 0:
        break


i = 0
j = len(m_s) - 1

while i != len(w_b):
    if w_b[i] < (m_s[j] * -1):
        cnt += 1
        i += 1
        j -= 1

    else:
        j -= 1

    if j < 0:
        break

print(cnt)
