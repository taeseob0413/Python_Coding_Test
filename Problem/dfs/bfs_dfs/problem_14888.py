"""
연산자 끼워 넣기
N개의 수가 주어지고 N-1개의 자리에 연산자 4개(+,-,*,//)를 넣을 수 있음.
연산은 우선순위가 없이 무조건 왼쪽에서부터 시작을 하고 나눗셈음 정수 나눗셈만을 취한다.

>>N의 갯수가 2~11이므로 시간복잡도는 일단 생각하지 않아도 됨. >>dfs로 문제를 해결할 수 있음.
"""
n=int(input())
num_list=list(map(int,input().split()))
operation_list=list(map(int,input().split()))

max_num=-int(1e9)
min_num=int(1e9)


def dfs(result,num_l,operaions):
    global max_num
    global min_num
    o1,o2,o3,o4=operaions
    if len(num_l)<=0:
        if result>max_num:
            max_num=result
        if result<min_num:
            min_num=result
    else:
        a=num_l[0]
        if o1>=1:
            dfs(result+a,num_l[1:],[o1-1,o2,o3,o4])
        if o2>=1:
            dfs(result-a,num_l[1:],[o1,o2-1,o3,o4])
        if o3>=1:
            dfs(result*a,num_l[1:],[o1,o2,o3-1,o4])
        if o4>=1:
            if result<0:
                l=-((-result)//a)
                dfs(l,num_l[1:],[o1,o2,o3,o4-1])
            else:
                l=result//a
                dfs(l,num_l[1:], [o1,o2,o3,o4-1])

dfs(num_list[0],num_list[1:],operation_list)
print(max_num)
print(min_num)