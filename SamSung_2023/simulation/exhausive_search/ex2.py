"""
행복한 수열의 개수
"""
n,m=map(int,input().split())
graph=[]

for _ in range(n):
    graph.append(list(map(int,input().split())))

def get_of_number_row(row,count):
    numbers=1
    max_cnt=1
    for i in range(1,n):
        if graph[row][i-1]==graph[row][i]:
            numbers+=1
        else:
            numbers=1
        max_cnt=max(max_cnt,numbers)

    return max_cnt>=count



def get_of_number_col(col, count):
    numbers = 1
    max_cnt=1
    for i in range(1, n):
        if graph[i-1][col] == graph[i][col]:
            numbers += 1
        else:
            numbers = 1
        max_cnt=max(max_cnt,numbers)

    return max_cnt>=count

result=0

for i in range(n):
    if get_of_number_row(i,m):
        result+=1
    if get_of_number_col(i,m):
        result+=1

print(result)

