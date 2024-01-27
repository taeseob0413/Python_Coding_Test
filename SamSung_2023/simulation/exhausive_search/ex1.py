n=int(input())
graph=[]

for _ in range(n):
    graph.append(list(map(int,input().split())))

def get_num_of_coin(row,col):
    num_of_coin=0

    for i in range(row,row+3):
        for j in range(col,col+3):
            num_of_coin+=graph[i][j]
    return num_of_coin

max_of_coin=0

for r in range(n):
    for c in range(n):
        if r+2<n and c+2<n:
            max_of_coin=max(max_of_coin,get_num_of_coin(r,c))

print(max_of_coin)