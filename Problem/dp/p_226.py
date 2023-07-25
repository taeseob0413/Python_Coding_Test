"""
효율적인 화폐구성!!
"""
INF=int(1e9)
d=[INF]*(10001)

n,m=map(int,input().split())
coin_list=[]

for _ in range(n):
    coin_list.append(int(input()))

#코인 초기화
for coin in coin_list:
    d[coin]=1

for i in range(1,10001):
    if d[i]!=INF:
        for coin in coin_list:
            if i+coin<=10000:
                d[i+coin]=min(d[i+coin],d[i]+1)

if d[m]==INF:
    print(-1)
else:
    print(d[m])