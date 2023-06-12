"""
효율적인 화폐구성
동전의 갯수 N과 원하는 금액 M이 주어질 때 주어진 동전의 종류를 사용하여 M원을 만드려고 한다.
이때 M원을 만들기 위한 최소한의 동전의 갯수구하기
1<=N<=100, 1<=M<=1000

이 문제의 경우에는 O(MN)의 시간복잡도 즉 100만번의 계산안에 문제를 해결할 수 있음
"""

n,m=map(int,input().split())
coin_list=[]
d=[0]*(10001)
#coin_list 초기화 & 초기 동전으로 만들수 있는 금액 초기화
for _ in range(n):
    coin=int(input())
    coin_list.append(coin)
    d[coin]=1
for i in range(1,10001):
    if d[i]!=0:
        for j in coin_list:
            if i+j<=10000:
                if d[i+j]==0:
                    d[i+j]=d[i]+1
                else:
                    d[i+j]=min(d[i]+1,d[i+j])
if d[m]==0:
    print(-1)
else:
    print(d[m])