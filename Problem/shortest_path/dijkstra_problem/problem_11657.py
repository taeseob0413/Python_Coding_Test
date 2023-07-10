"""
타임머신 문제

최단 거리 문제중 간선이 음의 정수도 포함된 형태의 문제
특히 문제의 출력 조건에서 음의 순환이 있을 경우 -1을 출력하도록 되어 있기 때문에 만드시 벨만 포트 알고리즘을 사용하여야 함.
"""

import sys

INF=int(1e9)
input=sys.stdin.readline

v,e=map(int,input().split())
edges=[]
dis=[INF]*(v+1)

for _ in range(e):
    a,b,c=map(int,input().split())
    edges.append((a,b,c))

def bellman_ford(start):
    dis[start]=0

    for i in range(v):
        for j in range(e):
            cur_node=edges[j][0]
            next_node=edges[j][1]
            cost=edges[j][2]

            if dis[cur_node]!=INF and dis[next_node]>dis[cur_node]+cost:
                dis[next_node]=dis[cur_node]+cost
                if i==v-1:
                    return True
    return False

result=bellman_ford(1)

if result:
    print(-1)
else:
    for i in range(2,v+1):
        if dis[i]>=INF:
            print(-1)
        else:
            print(dis[i])
