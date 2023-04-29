## 최고의 피자 :  1원당 열량이 가장 높은 피자


## 입력


top_num = int(input()) ## 토핑 종류 개수

dough_price, top_price = map(int, input().split()) ## 도우 가격, 토핑 가격

dough_cal = int(input())  ## 도우 열량


top_cals = []  ## 토핑 열량
for i in range(top_num):
    top_cals.append(int(input()))

## 토핑 열량 정렬

top_cals.sort()


max_pizza_cal_by_won = dough_cal / dough_price

for i in range(top_num):
    
    max_pizza_price = dough_price + top_price*i  ## 피자 가격 = 도우 가격 + 토핑 숫자*각 토핑 가격
    top_cal_sum = sum(top_cals[-i+1:])  ## 최대 토핑 열량 = 오름차순 정렬한 열량들에서 뒤에부터 토핑 개수만큼 합
    max_pizza_cal = dough_cal + top_cal_sum

    result = max_pizza_cal/max_pizza_price
    max_pizza_cal_by_won = max(result, max_pizza_cal_by_won)

print(max_pizza_cal_by_won)
