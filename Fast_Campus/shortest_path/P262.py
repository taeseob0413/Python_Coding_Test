"""
전보 문제

N개의 도시가 존재하고 각 도시를 잇는 도로가 존재(도로는 단방향)
이때 C라는 도시에서 위급 상황이 발생하여 모든 도시로 전보를 보내고자 할 때 전보를 받을 수 있는 도시의 갯수를 출력하는 문제
도시의 갯수 = 30000, 통로의 갯수 =20만

>>이 문제는 N이 크다는 점과 특정 도시로부터 출발한다는 점에서 다익스트라 알고리즘을 사용하면 된다.
>>이 경우에는 ElogV = 20만*log3만 이므로 시간 제한에 맞게 문제를 해결할 수 있다.
"""
import sys
import heapq

INF=int(1e9)
input=sys.stdin.readline

n,m,start=map(int,input().split())

dis=[INF]*(n+1)
graph=[[] for _ in range(n+1)]

for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))

def dijk(start):
    q=[]
    heapq.heappush(q,(0,start))
    dis[start]=0

    while q:
        dist,now=heapq.heappop(q)

        if dist>dis[now]:
            continue

        for i in graph[now]:
            cost=dis[now]+i[1]
            if dis[i[0]]>cost:
                dis[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

dijk(start)

count=0
max_value=-1

for i in range(1,n+1):
    if dis[i]<INF:
        count+=1
        if dis[i]>max_value:
            max_value=dis[i]

print(count-1,max_value)