# 2831 댄스파티
# 절댓값 공부
import sys
# from collections import deque
input = sys.stdin.readline

# 음수면 자기보다 작은 사람과 춤추길 원함
# 양수면 자기보다 큰 사람과 춤추길 원함

# 키가 같은 여자 남자는 춤출 수 X

n = int(input()) # 쌍의 수
man_info = list(map(int, input().split())) # 남자 쌍
woman_info = list(map(int, input().split())) # 여자 쌍
cnt = 0

# 남녀 음수 양수 구분
man_minus = []
woman_minus = []
man_plus = []
woman_plus = []
for m in man_info:
    if m > 0 : man_plus.append(m)
    if m < 0 : man_minus.append(m)
for w in woman_info:
    if w > 0 : woman_plus.append(w)
    if w < 0 : woman_minus.append(w)

# 정렬
man_plus.sort()
man_minus.sort(reverse=True)
woman_plus.sort()
woman_minus.sort(reverse=True)

i= 0
while man_plus: #man_plus가 사라질 때까지
    if len(woman_minus) == 0: break
    j = 0
    while woman_minus:
        if -woman_minus[-1] <= man_plus[i]:
            woman_minus.clear() # 이제 필요 없음
            break
        if man_plus[i] < -woman_minus[j]:
            cnt += 1
            man_plus.remove(man_plus[i])
            woman_minus.remove(woman_minus[j])
            j = 0
        else : j+=1
    i+=1

i= 0
while woman_plus:
    if len(man_minus) == 0: break
    j = 0
    while man_minus:
        if -man_minus[-1] <= woman_plus[i]:
            man_minus.clear() # 이제 필요 없음
            break
        if woman_plus[i] < -man_minus[j]:
            cnt += 1
            woman_plus.remove(woman_plus[i])
            man_minus.remove(man_minus[j])
            j = 0
        else : j+=1
    i+=1
    
print(cnt)
