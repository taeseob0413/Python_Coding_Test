"""
금광 문제

nXm 크기의 금광이 존재
첫번째 열의 임의의 행에서 시작하여 m번에 걸쳐서 오른쪽 위, 오른쪽 아래, 오른쪽 중 세가지 방향으로 이동.
결과적으로 채굴자가 얻을 수 있는 금의 최대 크기를 출력하는 문제.

>>바텀업 방식으로 문제를 풀 수 있음
>>
"""
t=int(input())
def max_gold(gold,n,m):
    d=[[0]*m for _ in range(n)]

    for i in range(n):
        d[i][0]=gold[i][0]

    for i in range(1,m):
        for j in range(n):
            if j-1>=0:
                d[j][i]=max(d[j][i],d[j-1][i-1]+gold[j][i])
            if j+1<n:
                d[j][i] = max(d[j][i], d[j + 1][i - 1] + gold[j][i])
            d[j][i]=max(d[j][i],d[j][i-1]+gold[j][i])

    max_value=d[0][m-1]
    for i in range(1,n):
        max_value=max(max_value,d[i][m-1])
    return max_value

for _ in range(t):
    n,m=map(int,input().split())
    gold=list(map(int,input().split()))
    g=[]

    for i in range(n):
        g.append(list(gold[i*m:i*m+m]))

    print(max_gold(g,n,m))
