"""
숨바꼭질 문제

수빈이는 현재 점 N(0~십만) , 동생은 점 K(0~십만)일 때 수빈이는 걷거나 순간이동 가능
수빈이가 걷는 다면 x-1 or x+1로 이동가능 / 순간이동을 하는 경구에는 1초 뒤에 2*x로 이동가능
"""
import sys
from collections import deque

input=sys.stdin.readline
INF=int(1e9)
n,k=map(int,input().split())

dis=[INF]*(200001)

q=deque()
dis[n]=0
q.append(n)
result=0
while q:
    now=q.popleft()
    if now == k:
        break
    if now-1>=0 and dis[now-1]>dis[now]+1:
        dis[now-1]=dis[now]+1
        q.append(now-1)

    if now+1<=200000 and dis[now+1]>dis[now]+1:
        dis[now+1]=dis[now]+1
        q.append(now+1)

    if now*2<=200000 and dis[now*2]>dis[now]+1:
        dis[now*2]=dis[now]+1
        q.append(now*2)


print(dis[k])

#시간 복잡도는 모든 노드를 O(len(d)) 이므로 20만번의 연산 안에 끝난다.
#dis의 크기를 20만으로 잡은 이유는 아무리 멀리 떨어져 있어도 10만번의 연산안에 끝나게 된다. 이는 어디서 시작을 하던지 거리가 20만인 점 까지는 고려할 필요가 없음을 의미
