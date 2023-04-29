n = int(input())

scv = list(map(int, input().split()))
cnt = 0
while 1:
    flag = 0
    for x in scv:
        if x > 0:
            flag = 1
    if flag == 0:
        break
    scv = sorted(scv, reverse=True)
    for i in range(len(scv)):
        if i == 0:
            scv[i] -= 9
        elif i == 1:
            scv[i] -= 3
        else:
            scv[i] -= 1
    
    cnt += 1

print(cnt)
