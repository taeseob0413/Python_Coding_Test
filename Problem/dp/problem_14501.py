"""
퇴사 문제

N일동안 일을 하게 될 때 걸리는 시간 T와 가치 P가 주어질 때 N일동안 가장 가치가 높은 일을 할 수 있도록 구성하기.

"""
n=int(input())
labor=[]
for _ in range(n):
    labor.append(list(map(int,input().split())))
d=[0]*(n+1)

for i in range(n):
    for j in range(i+labor[i][0],n+1):
        d[j]=max(d[j],d[i]+labor[i][1])
print(d[n])
