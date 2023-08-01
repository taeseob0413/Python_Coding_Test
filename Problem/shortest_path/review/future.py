""""
미래도시 2번쨰

N개의 도시와 M개의 도로가 주어진다.
회사원은 1번 도시에서 출발하여 K번 회사를 지나 X번 회사에 도착을 하여야 한다.
이때 최단 거리를 구하는 문제

>>이 문제의 경우에는 N,M이 전부 100이하이므로 플로이드 워셜(V^3)으로 구할 수 있다.
>>풀이에서 다익스트라와 플로이드 두 가지 경우 모두로 풀어볼 예정.
"""
import sys
import heapq

INF=int(1e9)
input=sys.stdin.readline

v,e=map(int,input().split())
graph1=[[] for _ in range(v+1)]
graph2=[[INF]*(v+1) for _ in range(v+1)]


for _ in range(e):
    a,b=map(int,input().split())
    #양방향 도로로 연결
    graph1[a].append((b,1))
    graph1[b].append((a,1))
    graph2[a][b],graph2[b][a]=1,1

x,k=map(int,input().split())

for i in range(v+1):
    graph2[i][i]=0

for t in range(1,v+1):
    for i in range(1,v+1):
        for j in range(1,v+1):
            graph2[i][j]=min(graph2[i][j],graph2[i][t]+graph2[t][j])

if graph2[1][k]+graph2[k][x]>=INF:
    print(-1)
else:
    print(graph2[1][k]+graph2[k][x])

def dijk(start,target):
    dis = [INF] * (v + 1)
    dis[start]=0
    q=[]
    heapq.heappush(q,(0,start))

    while q:
        dist,now=heapq.heappop(q)
        if dist>dis[now]:
            continue
        for i in (graph1[now]):
            cost=i[1]+dis[now]
            if cost<dis[i[0]]:
                dis[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

    return dis[target]

a1,a2=dijk(1,k),dijk(k,x)
if a1+a2>INF:
    print(-1)
else:
    print(a1+a2)