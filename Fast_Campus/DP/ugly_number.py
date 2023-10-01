"""
못생긴 수
"""
n=int(input())

num_list=[2,3,5]

start=1
dp=[0]*(n)

#맨 처음 못 생긴수는 1
dp[0]=1
result=0
#2,3,5가 곱해지는 dp의 각각의 인덱스
n1,n2,n3=0,0,0

for i in range(1,n):
    a,b,c=dp[n1]*2,dp[n2]*3,dp[n3]*5

    dp[i]=min(a,b,c)
    if dp[i]==a:
        n1+=1
    if dp[i]==b:
        n2+=1
    if dp[i]==c:
        n3+=1
    print(dp[i])
print(dp[n-1])

