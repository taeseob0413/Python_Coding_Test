"""
정확한 순위 문제

N명의 학생이 주어지고 각 학생의 성적 비교 횟수 M이 주어진다.
이때 성적을 확실하게 알 수 있는 학생을 구하기

>>성적을 활실하게 안다는 의미는 특정 학생으로 시작하여 다른 특정 학생들로 갈 수 있는 경로가 존재할 경우에 가능하다.
>>이때 N의 개수가 500이고 M이 10000이하 이므로 O(V^3)의 플로이드 워셜로는 풀 수가 없음.
>>각각의 학생들에 대하여 다익스트라를 사용한 뒤에 거리에서 INF가 없는 경우에 가능.
>>O(NElogN) : 500*10000*log500 의 경우에는 500*10000*9인 4500만 번의 연산을 통해 구할 수 있고 이는 제한시간이 5초인 문제
>>즉 1억번의 연산안에 해결할 수 있으므로 가능하다.
"""
import sys
import heapq

input=sys.stdin.readline
INF=int(1e9)

n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]


for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append((b,1))
    graph[b].append((a, 1))


def dijkstra(start):
    global n
    count=0
    dis=[INF]*(n+1)
    q=[]
    dis[start]=0
    heapq.heappush(q,(0,start))
    while q:
        dist,now=heapq.heappop(q)
        if dist>dis[now]:
            continue
        for i in graph[now]:
            cost=dis[now]+i[1]
            if cost<dis[i[0]]:
                dis[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

    for i in range(1,n+1):
        if dis[i]!=INF:
            count+=1
        else:
            break

    if count==n:
        print(start,end=' ')

for i in range(1,n+1):
    dijkstra(i)
