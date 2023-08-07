"""
좌표 정렬하기 문제
"""

n=int(input())
lo_list=[]

for _ in range(n):
    x,y=map(int,input().split())
    lo_list.append((x,y))

lo_list.sort(key=lambda x:(x[0],x[1]))

for i in lo_list:
    print(i[0], i[1])
