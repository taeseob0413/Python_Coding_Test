"""
정확한 순위 문제
N명의 학생이 존재(500이하)
이때 선생님은 N명의 학생의 성적을 분실했고 대신 M번의 학생의 비교를 통한 결과만 알고 있다.
정확한 등수를 알 수 있는 학생의 수를 구하는 문제.

>>이 문제에서 정확한 등수를 알 수 있다는 것은 a를 예로 들었을 경우에 a에서 나머지 n-1의 학생들까지 이어진 경로가 있어야 한다
>>이때의 경로는 a로 오는 경로, a에서 출발하는 경로 둘 중에 하나만 있으면 된다.
>>사이클은 생성될 수 없음. 사이클이 형성될 경우에는 등수에서 모순이 발생한다.
>>다익스트라를 이용하면 매 학생 500*1만*log500 < 5000만 이므로 알맞게 풀 수 있음.
"""
import heapq
import sys

INF=int(1e9)
input=sys.stdin.readline

n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append((b,1))

def dijk(start):
    global n
    dis=[INF]*(n+1)

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

    return dis

result=[]
result.append([])
for i in range(1,n+1):

    result.append(dijk(i))

num=0
for i in range(1,n+1):
    count=0
    for j in range(1,n+1):
        if result[i][j]!=INF or result[j][i]!=INF:
           count+=1
    if count==n:
        num+=1
print(num)
