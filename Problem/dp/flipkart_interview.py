"""
금광 문제
nxm 크기의 금광이 주어질 때 시작은 맨 처음열의 어떤행에서도 출발이 가능하다.
이때 다음 단계에서는 오른쪽, 오른쪽 위, 오른쪽 아래 세 방향으로 이동할 수 있다.

m열의 모든 금광의 금까지 획득했을 때 얻을 수 있는 최대 금의 개수를 구하는 문제
이 문제의 경우에는 T가 1000이하이고 n,m이 20이하이므로 시간복잡도는 크게 신경쓰지 않아도 되는 문제이다.
"""

t=int(input())

for _ in range(t):
    #1차원 리스트 > 2차원 리스트
    n,m=map(int,input().split())
    tmp=list(map(int,input().split()))
    gold=[]
    count=0
    sub = []
    d=[[0]*m for _ in range(n)]
    for i in range(len(tmp)):
        sub.append(tmp[i])
        count+=1
        if count==m:
            gold.append(sub)
            count=0
            sub=[]

    for i in range(n):
        d[i][0]=gold[i][0]

    for i in range(1,m):
        for j in range(n):
            if j-1>=0:
                d[j][i]=max(d[j][i],d[j-1][i-1]+gold[j][i])
            if j+1<n:
                d[j][i] = max(d[j][i], d[j+1][i-1] + gold[j][i])
            d[j][i]=max(d[j][i],d[j][i-1]+gold[j][i])


    max_num=d[0][m-1]
    for i in range(1,n):
        if max_num<d[i][m-1]:
            max_num=d[i][m-1]
    print(max_num)