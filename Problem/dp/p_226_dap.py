"""
효율적인 화폐구성 답안

모든 동전에서 하나씩 그 동전으로 만들 수 있는 모든 경우를 설정함.
"""
n,m=map(int,input().split())
coins=[]
for _ in range(n):
    coins.append(int(input()))


d=[10001]*(m+1)
d[0]=0

for i in range(len(coins)):
    for j in range(coins[i],m+1):
        if d[j-coins[i]]!=10001:
            d[j]=min(d[j],d[j-coins[i]]+1)

if d[m]==10001:
    print(-1)
else:
    print(d[m])