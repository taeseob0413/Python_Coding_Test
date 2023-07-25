"""
퇴사 문제
"""

n=int(input())
work=[]
for _ in range(n):
    a,b=map(int,input().split())
    work.append((a,b))
"""
d=[0]*(n+1)

for i in range(n):
    for j in range(i+work[i][0],n+1):
        d[j]=max(d[j],d[i]+work[i][1])
print(d[n])
"""

d1=[0]*(n+1)

for i in range(1,n+1):
    for j in range(i):
        if j+work[j][0]<=i:
            d1[i]=max(d1[i],d1[j]+work[j][1])
        else:
            d1[i]=max(d1[i],d1[j])
print(d1[n])