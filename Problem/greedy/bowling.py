"""
볼링공 고르기
N개의 볼링공이 주어지고 볼링공의 무게는 1~M일 때
두 사람은 각각 다른 무게의 공을 고르려고 한다. 이때 가짓수를 구하는 문제
(N은 1000이하 M은 10이하)

"""
n,m=map(int,input().split())
ball=list(map(int,input().split()))
ball_count=[0]*(m+1)

#O(n)
for i in range(len(ball)):
    ball_count[ball[i]]+=1

ball_set=set(ball)
ball=list(ball_set)
ball.sort()

result=0
for i in range(len(ball)-1):
    for j in range(i+1,len(ball)):
        result+=ball_count[ball[i]]*ball_count[ball[j]]
print(result)
