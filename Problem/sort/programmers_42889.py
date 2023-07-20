"""
실패율 문제
"""

def solution(N, stages):
    answer = []
    result=[]
    count_sort=[0]*(N+2)
    for i in stages:
        count_sort[i]+=1

    people=len(stages)

    for i in range(1,N+1):
        if people==0:
            result.append((i,0))
        else:
            result.append((i,count_sort[i]/people))
            people-=count_sort[i]
    result.sort(key=lambda x:(-x[1],x[0]))

    for a,b in result:
        answer.append(a)


    return answer

print(solution(4,[4,4,4,4,4]))