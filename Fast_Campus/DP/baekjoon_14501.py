"""
퇴사 문제

기간대비 금액이 높은 것들을 먼저 처리하는 것이 아님(즉 그리디 알고리즘이 아닌 문제)
모든 경우를 찾아봐야 하는 문제 >> 완전 탐색문제 >> DP생각해보기
"""
import sys

input=sys.stdin.readline

n=int(input())

work_list=[]
for _ in range(n):
    work_list.append(list(map(int,input().split())))

dp=[0]*(n+1)

for i in range(n):
    if i+work_list[i][0]<=n:
        for j in range(i+work_list[i][0],n+1):
            dp[j]=max(dp[j],dp[i]+work_list[i][1])

print(dp[n])
