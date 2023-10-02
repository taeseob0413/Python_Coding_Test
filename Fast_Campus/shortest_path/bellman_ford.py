"""
벨만 포드 알고리즘 코드

작동 원리
1. 출발 노드 설정
2. 최단 거리 table 초기화
3. 다음 과정을 n-1번 반복  >>  모든 간선에 대해서 확인 후 최단 거리 테이블 갱신
4. 만약 음의 순환을 확인하고 싶다면 3의 과정을 한번 더 수행하여 최단거리 table이 갱신될 경우 음의 순환이 존재하는 것.
"""
import sys

input=sys.stdin.readline
INF=int(1e9)

v,e=map(int,input().split())
dis=[INF]*(v+1)
edges=[]

for _ in range(e):
    edges.append(list(map(int,input().split())))

def bellman_ford(start):
    dis[start]=0
    for i in range(v):
        for j in range(e):
            cur_node=edges[j][0]
            next_noed=edges[j][1]
            dist=edges[j][2]

            if dis[cur_node]!=INF and dis[next_noed]>dist+dis[cur_node]:
                dis[next_noed]=dist+dis[cur_node]
                if i==v-1:
                    return True
    return False
