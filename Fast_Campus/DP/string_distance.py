"""
편집 거리 문제

A,B문자열이 주어질 때 A를 편집하여 B로 만들수 있는 최소 횟수를 구하는 문제
1. 삽입 2. 삭제 3. 교체의 3가지 방법을 이용할 수 있다.
"""

str1=input()
str2=input()

dp=[[0]*(len(str2)+1) for _ in range(len(str1)+1)]

for i in range(len(str2)+1):
    dp[0][i]=i

for j in range(len(str1)+1):
    dp[j][0]=j

for a in range(1,len(str1)+1):
    for b in range(1,len(str2)+1):
        if str1[a-1]==str2[b-1]:
            dp[a][b]=dp[a-1][b-1]
        else:
            #교체,삭제,삽입
            dp[a][b]=min(dp[a-1][b-1],dp[a-1][b],dp[a][b-1])+1
print(dp[len(str1)][len(str2)])
