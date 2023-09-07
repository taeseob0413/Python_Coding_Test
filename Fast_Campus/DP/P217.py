"""
1로 만들기

정수 X가 주어질 때 정수 X에 사용할 수 있는 연산은 다음과 같이 4가지이다.

1. X가 5로 나누어떨어지면, 5로 나누기
2. X가 3으로 나누어 떨어지면, 3으로 나누기
3. X가 2로 나누어 떨어지면, 2로 나누기
4. X에서 1을 빼기

연산의 최소 횟수를 구하는 문제

>> 이 문제의 경우에는 얼핏보면 그리디 알고리즘이라고 생각했음.
>> 이유는 5로 나누는 것이 가장 숫자를 작게 만드는 방법이기 때문임.
>> 반례를 생각하여 보니 만약 24라는 숫자가 있을 경우 3으로 나누는 것이 가장 좋음
>> 즉 완전 탐색으로 모든 경우를 다 조사해야 하는 경우임.
>> 탑다운으로 DP테이블을 구현하여 문제를 해결하였음.
"""
import sys

input=sys.stdin.readline
INF=int(1e9)

x=int(input())
dp=[INF]*(x+1)

def target_1(x,count):
    if x==1:
        dp[x]=min(dp[x],count+1)
    if x<=0:
        return
    if x%5==0:
        dp[x//5]=min(dp[x//5],count+1)
        target_1(x//5,count+1)
    if x%3==0:
        dp[x // 3] = min(dp[x // 3], count + 1)
        target_1(x // 3, count + 1)
    if x%2==0:
        dp[x // 2] = min(dp[x // 2], count + 1)
        target_1(x // 2, count + 1)
    dp[x-1]=min(dp[x-1],count+1)
    target_1(x-1, count + 1)
target_1(x,0)
print(dp[1])

#보텀업 방식
n=int(input())
dp=[0]*(30001)

for i in range(2,n+1):
    dp[i]=dp[i-1]+1

    if i%2==0:
        dp[i]=min(dp[i],dp[i//2]+1)
    if i%3==0:
        dp[i]=min(dp[i],dp[i//2]+1)
    if i%5==0:
        dp[i]=min(dp[i],dp[i//5]+1)

print(dp[n])