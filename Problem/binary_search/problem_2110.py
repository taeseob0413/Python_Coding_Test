"""
공유기 문제
N개의 집이 주어지고 C개의 공유기를 N개의 집에 적당하게 설치해서 가장 인접한 두 공유기 사이의 거리를 최대로 하는 문제

N은 20만이하 공유기의 갯수 C는 N이하 집의 좌표는 10억이하이다.
>>집의 좌표 즉 데이터가 10억이하 이므로 logN의 시간 복잡도를 갖는 이진탐색을 사용하면 좋을 듯 함.
"""
import heapq

n,c=map(int,input().split())
num_list=[]
for _ in range(n):
    num_list.append(int(input()))
max_dis=0
#Nlog(10억)<=600만
def binary_search(start,end,array,x):
    global max_dis
    while start<=end:
        count = 1
        tmp = array[0]
        mid = (start + end) // 2
        for i in range(1,len(array)):
            if array[i]-tmp>=mid:
                tmp=array[i]
                count+=1
            if count>=x:
                break
        if count>=x:
            start=mid+1
            max_dis=mid
        elif count<x:
            end=mid-1
#Nlog(N)
num_list.sort()
binary_search(0,num_list[-1]-num_list[0],num_list,c)
print(max_dis)
