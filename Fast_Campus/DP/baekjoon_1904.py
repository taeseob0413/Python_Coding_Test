"""
백준 01타일

>> 모든 경우를 다 봐야하기 때문에 DP로 풀면 풀 수 있음
"""
import sys

input=sys.stdin.readline

n=int(input())
dp=[0]*(n+1)

dp[1]=1
dp[2]=2

for i in range(3,n+1):
    dp[i]=(dp[i-1]+dp[i-2])%15746

print(dp[n])

