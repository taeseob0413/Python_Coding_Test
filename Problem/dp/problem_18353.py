"""
병사 배치 문제

N명의 병사가 각각 전투력이 주어진채로 주어질 때 최소의 병사를 제거하여 오름차순의 형태가 되도록 병사를 나열하기

전형적인 LIS 증가하는 부분 수열 문제
"""
n=int(input())
num_list=list(map(int,input().split()))
d=[1]*n

for i in range(1,n):
    for j in range(i):
        if num_list[j]>num_list[i]:
            d[i]=max(d[i],d[j]+1)
print(n-max(d))

