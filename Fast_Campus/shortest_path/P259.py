"""
미래 도시 문제

1번 도시에서 출발하여 K번 도시를 거쳐 X번 도시까지로 가는 최단거리를 구하는 문제
각 도시의 도로는 양방향으로 이동이 가능하고 도로는 1초의 시간을 갖고 이동이 가능하다.

>>이 문제의 경우에는 N이 100이하이므로 플로이드 워셜을 사용하여 graph[1][k]+graph[k][x]로 구해도 가능하다.
>>시간을 좀 더 줄이기 위해서는 다익스트라 알고리즘을 두번 사용하는 것도 괜찮음.
"""
import sys
import heapq

INF=int(1e9)
input=sys.stdin.readline

n,m=map(int,input().split())

#플로이드 워셜일 이용한 문제 풀이 그래프
graph_f=[[INF]*(n+1) for _ in range(n+1)]

#다익스트라를 이용한 문제 풀이 그래프
graph_d=[[] for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,input().split())
    graph_f[a][b]=1
    graph_f[b][a]=1
    graph_d[a].append((b,1))
    graph_d[b].append((a,1))

x,k=map(int,input().split())

#플로이드 워셜 이용한 문제 풀이
for i in range(1,n+1):
    graph_f[i][i]=0

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph_f[i][j]=min(graph_f[i][j],graph_f[i][k]+graph_f[k][j])

re=graph_f[1][k]+graph_f[k][x]

if re>=INF:
    print(-1)
else:
    print(re)

#다익스트라 이용한 문제 풀이
def dijkstra(start,end):
    dis=[INF]*(n+1)
    q=[]
    dis[start]=0
    heapq.heappush(q,(0,start))

    while q:
        dist,now=heapq.heappop(q)

        if dist>dis[now]:
            continue

        for i in graph_d[now]:
            cost=dist+i[1]
            if dis[i[0]]>cost:
                dis[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

    return dis[end]

re=dijkstra(1,k)+dijkstra(k,x)

if re>=INF:
    print(-1)
else:
    print(re)
