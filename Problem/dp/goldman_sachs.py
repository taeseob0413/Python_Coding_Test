"""
골드만 삭스 인터뷰

"""
a=input()
b=input()

dp=[[0]*(len(b)+1) for _ in range(len(a)+1)]

for i in range(1,len(b)+1):
    dp[0][i]=i

for j in range(1,len(a)+1):
    dp[j][0]=j

for i in range(1,len(a)+1):
    for j in range(1,len(b)+1):
        if a[i-1]==b[j-1]:
            dp[i][j]=dp[i-1][j-1]
        else:
            #교체,삽입
            dp[i][j]=min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])+1
print(dp[len(a)][len(b)])


