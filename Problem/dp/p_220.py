"""
개미전사 문제

dp테이블 d[n] >> n번째에 얻을 수 있는 최대 곡식량
d[n]=max(d[n-1],d[n-2]+food[n])
"""
n=int(input())
food=list(map(int,input().split()))
food_list=[0]+food
d=[0]*(n+1)
d[1]=food[1]

for i in range(2,n+1):
    d[i]=max(d[i-1],d[i-2]+food_list[i])
print(d[n])


