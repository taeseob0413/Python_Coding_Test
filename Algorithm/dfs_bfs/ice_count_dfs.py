"""
교재의 해답에서는 dfs를 이요하여 문제를 풀었음.
"""
#행,렬 입력받기
n,m=map(int,input().split())

#얼름틀 입력받기
ice_map=[]
for _ in range(n):
    ice_sub=list(map(int,input()))
    ice_map.append(ice_sub)

def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    if ice_map[x][y]==0:
        ice_map[x][y]=1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

result=0
for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:
            result+=1
print(result)