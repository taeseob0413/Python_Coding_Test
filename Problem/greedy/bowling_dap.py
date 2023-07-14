"""
볼링공 해설지 풀이

A가 어떤 공을 선택했을 때 전체에서 그 공의 갯수를 제외한 곳에서 B가 선택할 수 있는 걸 응용
"""
n,m=map(int,input().split())
data=list(map(int,input().split()))
count=[0]*(11)
for i in data:
    count[i]+=1
result=0
for j in range(1,11):
    n-=count[j]
    result+=count[j]*n
print(result)