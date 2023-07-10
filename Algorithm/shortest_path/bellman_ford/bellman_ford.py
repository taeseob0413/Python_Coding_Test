"""
벨만 포드 알고리즘.

벨만 포드 알고리즘은 음의 간선이 존재할 때 사용할 수 있는 최단거리 알고리즘이다.
다익스트라와의 차이점은 매 단계마다 모든 간선을 전부 확인한다는 데에 있다.
따라서 시간 복잡도는 O(VE)로 다익스트라보다 느리지만 음의 간선이 있는 경우 사용가능하고 음의 간선 순환 또한 찾아낼 수 있다.
또한 다익스트라가 제공하는 최적의 해를 항상 보장한다.

동작 원리
1. 출발노드 설정
2. 최단거리 table 초기화
3. 다음 과정을 N-1번 반복
-전체 간선 E개를 확인
-각 간선을 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신한다.
4. 만약 음의 간선 순환이 발생하는지 check하기 위해서는 3번 과정을 한번 더 수행한다.
- 이때 최단 거리 테이블이 갱신된다면 음의 간선 순환이 발생한 것.
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

            if dis[cur_node] !=INF and dis[next_node]>dis[cur_node]+cost:
                dis[next_node]=dis[cur_node]+cost
                #음의 간선 발생한 경우
                if i==v-1:
                    return True
    return False

