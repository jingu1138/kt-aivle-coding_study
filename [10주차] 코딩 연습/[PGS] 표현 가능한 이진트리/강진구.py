def solution(numbers):
    answer = []
    print(type(bin(10)[2:])) #2진수 변환 함수
    flag = 0
    for num in numbers:
        s = bin(num)[2:]
        if len(s)%2 != 0:
            level = len(s)-1
        else:
            level = len(s)
        for l in range(level,1,-1):
            if s[int(2**(l-1)-1)] == 0:
                flag = 0
        if flag == 0:
            answer.append(1)
        else:
            answer.append(0)
    
    return answer
