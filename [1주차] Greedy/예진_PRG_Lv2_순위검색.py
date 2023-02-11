# info: 지원자의 4가지 정보, 획득 코딩테스트 점수 (스페이스로 구분)
# query: 개발팀이 궁금해하는 문의조건 (and로 구분)

def solution(info, query):
    
    ans = [0] * len(query)
    men = list()
    
    # info 정보를 스페이스 기준으로 구분                                            
    for i in info:
        men.append(i.split())
    
    # 쿼리문 나누기 (and와 스페이스)
    for q in range(len(query)):
        message = query[q].split('and')
        message = message[:3] + message[3].split()
        
        for m in men:
            for i in range(5):
                if i == 4 and int(m[i]) >= int(message[i].strip()):
                    ans[q] += 1
                if message[i].strip() == '-':
                    continue
                if message[i].strip() != m[i]:
                    break
    
    return ans