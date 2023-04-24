import sys
input = sys.stdin.readline

n = int(input())

# 남자 키, 유형 입력
boy = list(map(int, input().split()))   
# 여자 키, 유형 입력
girl = list(map(int, input().split()))

cnt = 0
# 남, 여 각각 유형 별로 분류
boy_up = []
# boy_down = []
girl_up = []
# girl_down = []
# -를 +로 변경한 리스트 생성
boy_down_plus = []
girl_down_plus = []

for i in boy:
    if i > 0:
        boy_up.append(i)
    else:
        boy_down_plus.append(abs(i))
        
for i in girl:
    if i > 0:
        girl_up.append(i)
    else:
        girl_down_plus.append(abs(i))
        
# for i in boy_down:
#     boy_down_plus.append(abs(i))
    
# for i in girl_down:
#     girl_down_plus.append(abs(i))

# boy_up과 girl_down_plus
# boy_down_plus와 girl_up만 비교하면 된다.
a = len(boy_up)
b = len(boy_down_plus)
c = len(girl_up)
d = len(girl_down_plus)

if a >= d:
    x = d
else:
    x = a

if b <= c:
    y = b
else:
    y = c
    
    
# for i in range(0, x):
#     if boy_up[i] < girl_down_plus[i]:
#         cnt += 1

# for i in range(0, y):
#     if girl_up[i] < boy_down_plus[i]:
#         cnt += 1

print(cnt)
