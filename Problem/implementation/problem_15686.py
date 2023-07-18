"""
치킨 배달 문제
NxN 도시가 존재할 떄 M개의 치킨집만 남기고 최소의 치킨거리를 구하는 문제

>>이 문제는 N<=50이고 M<=13이므로 모든 경우의 탐색을 진행해보려고 하였음.
"""
from itertools import combinations
n,m=map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))

chi=[]
home=[]
for i in range(n):
    for j in range(n):
        if graph[i][j]==2:
            chi.append((i,j))
        elif graph[i][j]==1:
            home.append((i,j))

check=list(combinations(chi,m))

def get_sum(check):

    result=0
    for hx,hy in home:
        tmp = 1e9
        for cx,cy in check:
            tmp=min(tmp,abs(hx-cx)+abs(hy-cy))
        result+=tmp
    return result

rr=1e9
for che in check:
    rr=min(rr,get_sum(che))
print(rr)