"""
부품찾기 문제는 계수 정렬로도 풀 수 있음.
"""
n=int(input())
data_list=[0]*(1000001)
for i in input().split():
    data_list[int(i)]=1
m=int(input())
order_list=list(map(int,input().split()))
for j in order_list:
    if data_list[j]==1:
        print("yes")
    else:
        print("no")

