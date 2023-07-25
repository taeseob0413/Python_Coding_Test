"""
병사 배치하기 >> 가장 긴 증가하는 수열 문제
"""

n=int(input())
sol=list(map(int,input().split()))
d=[1]*(n)

for i in range(1,n):
    for j in range(i):
        if sol[i]<sol[j]:
            d[i]=max(d[i],d[j]+1)

print(n-max(d))