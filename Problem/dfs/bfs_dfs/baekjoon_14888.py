"""
연산자 끼워넣기 문제
"""

n=int(input())
num_list=list(map(int,input().split()))

#+,-,x,//
operation_list=list(map(int,input().split()))

max_num=-int(1e9)
min_num=int(1e9)
def dfs(result,num_list,operations):
    global max_num,min_num
    if len(num_list)<=0:
        max_num=max(max_num,result)
        min_num=min(min_num,result)
        return
    number=num_list[0]
    if operations[0]>=1:
        dfs(result+number,num_list[1:],[operations[0]-1,operations[1],operations[2],operations[3]])
    if operations[1]>=1:
        dfs(result - number, num_list[1:], [operations[0], operations[1]-1, operations[2], operations[3]])
    if operations[2]>=1:
        dfs(result * number, num_list[1:], [operations[0], operations[1], operations[2]-1, operations[3]])
    if operations[3]>=1:
        if result<=0:
            result=-((-result)//number)
        else:
            result=result//number
        dfs(result, num_list[1:], [operations[0],operations[1], operations[2], operations[3]-1])

dfs(num_list[0],num_list[1:],operation_list)
print(max_num)
print(min_num)