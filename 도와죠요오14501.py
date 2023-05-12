import sys

input = sys.stdin.readline

n = int(input())
lst = []

for _ in range(n):
    a, b = map(int, input().split())
    lst.append((a, b))


def ans(i):
    cnt = 0

    while (n + 1) - i != 0:
        if i + lst[i - 1][0] - 1 <= n:
            cnt += lst[i - 1][1]
            i += lst[i - 1][0]

        else:
            i += 1

    return cnt


mxcnt = 0

for j in range(1, n + 1):
    if ans(j) > mxcnt:
        mxcnt = ans(j)

print(mxcnt)
