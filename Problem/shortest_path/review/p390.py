"""
숨바꼭질 문제
"""
import heapq
import sys

input=sys.stdin.readline
INF=int(1e9)

n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
dis=[INF]*(n+1)

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append((b,1))
    graph[b].append((a, 1))

start=1
dis[start]=0
dis[0]=0
q=[]
heapq.heappush(q,(dis[start],start))

while q:
    dist,now=heapq.heappop(q)
    if dist>dis[now]:
        continue
    for i in graph[now]:
        cost=dist+i[1]
        if cost<dis[i[0]]:
            dis[i[0]]=cost
            heapq.heappush(q,(cost,i[0]))

count=0
max_value=max(dis)
index=0
for i in range(n,0,-1):
    if dis[i]==max_value:
        count+=1
        index=i
print(index,max_value,count)

