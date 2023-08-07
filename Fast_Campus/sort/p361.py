def solution(N, stages):
    # 총 인원
    total = len(stages)

    # 각 스테이지에 머물고 있는 인원을 계수정렬로 구현
    # 인덱스는 1~N+1까지가 필요.
    # O(N)>>20만
    peo = [0] * (N + 2)
    for i in stages:
        peo[i] += 1

    result = []
    for i in range(1, N + 1):
        if total!=0:
            fail = peo[i] / total
            result.append((fail, i))
            total -= peo[i]
        else:
            result.append((0,i))
    result.sort(key=lambda x: (-x[0], x[1]))

    answer = []
    for i in result:
        answer.append(i[1])


    return answer

