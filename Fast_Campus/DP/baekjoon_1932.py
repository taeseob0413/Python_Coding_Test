"""
정수 삼각혐 문제
"""
import sys

input=sys.stdin.readline


n=int(input())

num_list=[]
dp=[]

for i in range(n):
    num_list.append(list(map(int,input().split())))
    dp.append([0]*(i+1))

dp[0][0]=num_list[0][0]

for j in range(n-1):
    for k in range(j+1):
        dp[j+1][k]=max(dp[j+1][k],dp[j][k]+num_list[j+1][k])
        dp[j+1][k+1]=max(dp[j+1][k+1],dp[j][k]+num_list[j+1][k+1])

print(max(dp[n-1]))

