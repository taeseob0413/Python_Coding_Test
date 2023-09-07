"""
바닥 공사

이 문제의 경우에는 점화식을 세우면 DP로 쉽게 풀 수 있음.
"""

n=int(input())

dp=[0]*(1001)
dp[1]=1
dp[2]=3

for i in range(3,n+1):
    dp[i]=(dp[i-1]+dp[i-2]*2)%796796

print(dp[n])