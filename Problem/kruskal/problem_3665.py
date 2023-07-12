"""
최종 순위 문제

테스트 케이스 T가 주어지고 각 테스트 케이스의 구조는 다음과 같다(T<=100)
n >>팀의 수 / <=500
t1 t2 .... tn >>각 팀의 등수
m >> 상대 등수가 바뀐 횟수
a,b >> 상대 등수가 바뀐 팀의 번호

>>이번 문제는 위상정렬로 풀 수 있다고 생각. T*O(V+E)의 시간복잡도를 같기 때문에 충분히 가능.
>>진입 차수는 1등은 0 2등은 1 3등은 2 ...이런식으로 구현하면 된다.
>>처음에 계수 정렬로 풀었는데 이 경우에는 사이클이 발생하는 경루를 찾을 수 없음.
"""
t=int(input())

def topology_sort(indegree,grade,team,start):
    count=[0]*(len(grade))
    for a,b in team:
        if grade[a-1]<grade[b-1]:
            indegree[b]-=1
            indegree[a]+=1
        else:
            indegree[b]+=1
            indegree[a]-=1

    for i in range(1,len(indegree)):
        count[indegree[i]]+=1
    flag=True
    for i in range(len(count)):
        if count[i]!=1:
            flag=False
            break
    if flag:
        for i in range(1,len(indegree)):
            print(indegree[i]+1,end=' ')
    else:
        print("IMPOSSIBLE",end=" ")
    print()

for _ in range(t):
    n=int(input())
    indegree=[0]*(n+1)
    grade=list(map(int,input().split()))
    start=0
    #진입 차수 초기화
    for i in range(len(grade)):
        indegree[i+1]=grade[i]-1
        if grade[i]-1==0:
            start=i+1
    m=int(input())
    team=[]
    for _ in range(m):
        a,b=map(int,input().split())
        team.append((a,b))

    topology_sort(indegree,grade,team,start)