"""
금광 문제
"""

t=int(input())

for _ in range(t):
    n,m=map(int,input().split())
    geum=list(map(int,input().split()))
    data=[]

    #data초기화 과정
    for i in range(n):
        data.append(geum[4*i:4*i+m])

    #매 단계에서 리스트의 영역을 벗어날 경우에 a,b는 -1로 유지되면서 신경안써도 되는 영역이 됨.
    for y in range(1,m):
        for x in range(n):
            a,b,c=-1,-1,-1
            if x-1>=0:
                a=data[x-1][y-1]
            if x+1<n:
                b=data[x+1][y-1]
            c=data[x][y-1]

            data[x][y]=max(a,b,c)+data[x][y]
    max_value=-1
    for i in range(n):
        if max_value<data[i][m-1]:
            max_value=data[i][m-1]
    print(max_value)
