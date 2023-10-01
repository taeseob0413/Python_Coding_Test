"""
가장 긴 증가하는 부분 수열

수열 A가 주어질 때 가장 긴 증가하는 부분 수열을 구하는 문제

>>O(N^2)으로 풀이 가능
>>dp테이블의 dp[i]는 i번째 원소를 포함하였을 떄 만들 수 있는 가장 긴 부분 수열의 길이이다.
>>마지막은 max(dp)로 출력을 해야 답이 나옴.
"""

n=int(input())
num_list=list(map(int,input().split()))

dp=[1]*(n)

for i in range(1,n):
    for j in range(i):
        if num_list[i]>num_list[j]:
            dp[i]=max(dp[i],dp[j]+1)

print(max(dp))