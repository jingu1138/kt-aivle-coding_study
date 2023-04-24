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
        
        
boy_up.sort()
girl_up.sort()
boy_down_plus.sort()
girl_down_plus.sort()

# boy_up과 girl_down_plus
# boy_down_plus와 girl_up만 비교하면 된다.

# 커플변수
cnt = 0

# boy_up과 girl_down_plus 비교
left = 0
right = 0
while left < len(boy_up) and right < len(girl_down_plus):
    if (boy_up[left] < girl_down_plus[right]):
        cnt += 1
        left += 1
        right += 1
    else:
        right += 1

        
# boy_down_plus와 girl_up 비교
left = 0
right = 0
while left < len(boy_down_plus) and right < len(girl_up):
    if (boy_down_plus[left] > girl_up[right]):
        cnt += 1
        left += 1
        right += 1
    else:
        left += 1
    
print(cnt)
