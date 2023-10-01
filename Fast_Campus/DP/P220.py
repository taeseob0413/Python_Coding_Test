"""
개미 전사 문제

식량 창고가 일직선으로 이어져 있다. 이때 인접한 식량창고가 공격받으면 알아챌 수 있다.
정찰병에게 들키지 않고 식량창고를 약탈하기 위해서 최소한 한 칸 이상 떨어진 식량창고를 약탈해야 한다.
이때 얻을 수 있는 최대 식량의 수를 구하는 문제

>>이 문제의 경우에도 DP로 해결할 수 있음.
>>문제의 점화식을 DP테이블을 작성 후 dp[n]=max(dp[n-1],dp[n-2]+food[n])으로 점화식을 세울 수 있음.
"""

n=int(input())
food=list(map(int,input().split()))
dp=[0]*(n)
dp[0]=food[0]
dp[1]=max(food[0],food[1])

for i in range(2,len(food)):
    dp[i]=max(dp[i-1],food[i]+dp[i-2])

print(dp[n-1])