# 런타임 에러

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
m_s.sort(reverse=True)
w_s.sort(reverse=True)


cnt = 0
i = 0
j = 0

while i != len(m):

    if len(w_s) == 0:
        break

    if m[i] < (w_s[j] * -1) and m[i] != 0 and w_s[j] != 0:
        cnt += 1
        w_s[j] = 0
        j = 0
        i += 1

    else:
        if j < len(w_s):
            j += 1

        else:
            i += 1
            continue

i = 0
j = 0

while i != len(m_s):

    if len(m_s) == 0:
        break

    if (m_s[i] * -1) > w[j] and w[j] != 0 and m_s[i] != 0:
        cnt += 1
        w[j] = 0
        j = 0
        i += 1

    else:
        if j < len(w):
            j += 1

        else:
            i += 1
            continue


print(cnt)
