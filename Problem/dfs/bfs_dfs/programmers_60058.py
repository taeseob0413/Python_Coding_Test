"""
괄호 변환 문제
"""


def solution(p):
    answer = ''
    if len(p) == 0:
        return answer

    start = True
    c, d = 0, 0
    for i in p:
        if i == '(':
            c += 1
        else:
            d += 1
        if d > c:
            start = False
    if start:
        return p

    # 문자열 u의 올바른 문자열인지 check
    flag = True
    a, b = 0, 0
    u = ''
    v = ''
    for i in range(len(p)):
        if p[i] == '(':
            a += 1
        else:
            b += 1
        # b>a인 경우에는 올바른 문자열 X
        if b > a:
            flag = False
        if a == b:
            if i == len(p) - 1:
                u = p
                v = ''
            else:
                u = p[:i + 1]
                v = p[i + 1:]
            break
    if flag:
        answer += u + solution(v)
    else:
        answer += '(' + solution(v) + ')'

        for i in u[1:-1]:
            if i == '(':
                answer += ')'
            else:
                answer += '('
    return answer

print(solution(")("))