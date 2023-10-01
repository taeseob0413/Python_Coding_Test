"""
병사 배치하기 문제

병사의 수 N이 주어지고 N명의 병사의 전투력이 주어질 때
몇몇의 병사를 제거하여 병사의 전투력이 오름차순이 되도록 만드려고 한다.
이때 가장 최소한의 병사만 제거하여 최대의 병사수를 구하는 문제

>>LIS문제 dp테이블 초기화시 dp[i]는 i번째 병사를 포함했을 떄의 최대 경우의 수
"""

n=int(input())
army=list(map(int,input().split()))
dp=[1]*n

for i in range(1,n):
    for j in range(i):
        if army[i]<army[j]:
            dp[i]=max(dp[i],dp[j]+1)
print(n-max(dp))