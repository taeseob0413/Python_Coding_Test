"""
효율적인 화폐구성

N개의 화폐종류가 있을 때 이 화폐들을 이용하여 M원을 만들 때 필요한 동전의 최소 갯수를 구하는 문제.

>>예전에 그리디 알고리즘에서 풀었던 문제는 화폐가 각각 배수로 이루어져 있어서 무조건 큰 화폐의 단위부터 쓰는 것이 문제 풀이의 핵심이었지만
>>이 문제는 화폐가 각각 배수 관계가 아니기 때문에 모든 경우를 다 조사해야한다.
"""
INF=int(1e9)

n,m=map(int,input().split())
coins=[]
dp=[INF]*(10001)

for _ in range(n):
    coins.append(int(input()))

for coin in coins:
    dp[coin]=1
#O(n*10000) >> 백만번의 연산
for i in range(1,10001):
    if dp[i]!=INF:
        for coin in coins:
            if i+coin<10001:
                dp[i+coin]=min(dp[i+coin],dp[i]+1)

if dp[m]==INF:
    print(-1)
else:
    print(dp[m])

#해설지 풀이
dp1=[10001]*(m+1)
dp1[0]=0
for i in range(n):
    for j in range(coins[i],m+1):
        if dp1[j-coins[i]]!=10001:
            dp1[j]=min(dp1[j],dp1[j-coins[i]]+1)

if dp1[m]==10001:
    print(-1)
else:
    print(dp1[m])