"""
1로 만들기 문제
"""
n=int(input())

d=[30001]*(n+1)
d[1]=0
for i in range(1,n+1):
    if i+1<=n:
        d[i+1]=min(d[i]+1,d[i+1])
    if i*5<=n:
        d[i*5]=min(d[i]+1,d[i*5])
    if i*3<=n:
        d[i*3]=min(d[i]+1,d[i*3])
    if i*2<=n:
        d[i*2]=min(d[i]+1,d[i*2])
print(d[n])