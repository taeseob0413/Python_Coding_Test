"""
편안한 칸 문제
"""
n,m=map(int,input().split())

dx,dy=[0,1,0,-1],[1,0,-1,0]
graph=[[False]*n for _ in range(n)]

def samsung(x,y):
    count=0
    graph[x][y]=True

    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<len(graph) and 0<=ny<len(graph):
            if graph[nx][ny]==True:
                count+=1

    if count==3:
        return True

    return False

for _ in range(m):
    a,b=map(int,input().split())
    if samsung(a-1,b-1):
        print(1)
    else:
        print(0)
