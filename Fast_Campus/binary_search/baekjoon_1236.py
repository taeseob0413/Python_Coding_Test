"""
성지키기 문제

N,M의 성이 주어지고 각각의 성은 .,X로 구성되어 있다.
이떄 X는 경비원이 있음을 뜻한다.
모든 N행, M행 각각에 경비원을 배치하려고 할 때 최소로 추가해야 하는 경비원의 수

>>N행, M행 각각을 볼때 만약 N행에 4명 , M행에 3명의 경비원이 추가로 필요하다고 할 때
>>최소로 배치하기 위해서 N1,M1에 한명 N2,M2에 한명씩 배치해나가면 된다.
>>즉 N행과 M열에서 각각 필요한 경비원의 수를 구해서 둘 중의 큰 값이 정답이 되는 문제.
"""

n,m=map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(str,input())))

set_m=set()
set_n=set()

for i in range(n):
    for j in range(m):
          if graph[i][j]=="X":
              set_n.add(i)
              set_m.add(j)

print(max(n-len(set_n),m-len(set_m)))
