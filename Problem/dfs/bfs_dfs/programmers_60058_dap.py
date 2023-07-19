"""
프로그래머스 괄호변환 문제를 교재의 해답을 보고 내 풀이로 다시 변경
"""
#균형잡인 문자열 인덱스 반환
def balanced_string(p):
    a,b=0,0
    for i in range(len(p)):
        if p[i]=='(':
            a+=1
        else:
            b+=1
        if a==b:
            return i

#올바른 문자열인지 확인
def check_string(p):
    a,b=0,0
    for i in p:
        if i=="(":
            a+=1
        else:
            b+=1
        if b>a:
            return False
    return True

def solution(p):
    answer=''
    if len(p)==0:
        return answer
    index=balanced_string(p)
    u=p[:index+1]
    v=p[index+1:]

    if check_string(u):
        answer+=u
        answer+=solution(v)
    else:
        answer+='('
        answer+=solution(v)
        answer+=')'

        for i in u[1:-1]:
            if i=='(':
                answer+=')'
            else:
                answer+="("
    return answer
