"""
평범한 배낭 문제

>>이 문제의 핵심은 dp테이블을 2차원으로 생성해야 한다는 것
>>이유는 변수가 2개이기 때문..
"""

n,k=map(int,input().split())
products=[]

for _ in range(n):
    w,v=map(int,input().split())
    products.append((w,v))


dp=[[0]*(k+1) for _ in range(n+1)]

for i in range(1,len(products)+1):
    for j in range(k+1):
        if products[i-1][0]>j:
            dp[i][j]=dp[i-1][j]
        else:
            if j-products[i-1][0]>=0:
                dp[i][j]=max(dp[i-1][j],dp[i-1][j-products[i-1][0]]+products[i-1][1])

print(dp[n][k])
