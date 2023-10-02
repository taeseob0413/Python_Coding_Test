"""
타임 머신 문제

N = 도시의 갯수, M= 버스의 갯수가 주어질 때 최단 경로를 구하는 문제이다.
단 M이 0과 음수도 가능하고 무한히 시간을 오래전으로 되돌릴 수 있다면 -1을 출력하는 문제.

>> 이 경우에는 음의 간선이 존재하고 음의 순환도 체크해야 하기 때문에 벨만 포드 알고리즘을 사용하면 된다.
>> 또한 N=500, M=6000이므로 30만번의 연산으로 끝낼 수 있다.
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
            next_node=edges[j][1]
            cost=edges[j][2]
            if dis[cur_node] !=INF and dis[next_node]>dis[cur_node]+cost:
                dis[next_node]=dis[cur_node]+cost
                if i==v-1:
                    return True
    return False

if bellman_ford(1):
    print(-1)
else:
    for i in range(2,v+1):
        if dis[i]>=INF:
            print(-1)
        else:
            print(dis[i])