"""
전보 문제

N개의 도시가 존재(N<=3만)
이때 X,Y사이에 통로가 존재할 경우에 전보를 보낼 수 있다. (방향그래프)
어느 날 출발 도시에서 문제가 발생했을 경우에 전보를 보낼 수 있는 도시의 갯수와 도시들이 모두 메시지를 받는 데까지 걸리는 시간 구하는 문제

>>이 문제의 경우에는 다익스트라를 사용해야 시간복잡도를 충족시킬 수 있음.
>>도시들이 모두 메시지를 받는 데까지 걸리는 시간은 distance 테이블에서 INF가 아닌 가장 큰 값을 구하면 되는 문제
"""
import heapq
import sys

input=sys.stdin.readline
INF=int(1e9)

n,m,start=map(int,input().split())
graph=[[] for _ in range(n+1)]
dis=[INF]*(n+1)

for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))

def dijk(start):
    dis[start]=0
    q=[]
    heapq.heappush(q,(0,start))

    while q:
        dist,now=heapq.heappop(q)
        if dist>dis[now]:
            continue
        for i in graph[now]:
            cost=i[1]+dis[now]
            if cost<dis[i[0]]:
                dis[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

dijk(start)
count=0
max_time=0

for i in range(1,n+1):
    if dis[i]!=0 and dis[i]!=INF:
        count+=1
        if max_time<dis[i]:
            max_time=dis[i]
print(count,max_time)