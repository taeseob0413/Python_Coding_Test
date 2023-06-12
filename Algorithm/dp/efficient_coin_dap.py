"""
효율적인 동전 해설지 풀이
"""

n,m=map(int,input().split())
coin_list=[]
for _ in range(n):
    coin_list.append(int(input()))
d=[10001]*(m+1)
d[0]=0
for i in range(n):
    for j in range(coin_list[i],m+1):
        #j-coin_list[i]번째 동전을 만드는 방법이 존재할 때
        if d[j-coin_list[i]]!=10001:
            d[j]=min(d[j],d[j-coin_list[i]]+1)
if d[m]==10001:
    print(-1)
else:
    print(d[m])

