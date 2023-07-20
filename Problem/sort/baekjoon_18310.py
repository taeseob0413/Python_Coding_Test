"""
안테나 문제

>>퀵 정렬이용하여 정렬해보기
"""

def quick_sort(start,end,data):
    if start>=end:
        return
    pivot=start
    left=start+1
    right=end

    while left<=right:
        while left<=end and data[left]<=data[pivot]:
            left+=1
        while right>start and data[right]>=data[pivot]:
            right-=1

        if left>right:
            data[right],data[pivot]=data[pivot],data[right]
        else:
            data[left],data[right]=data[right],data[left]
    quick_sort(start,right-1,data)
    quick_sort(right+1,end,data)

n=int(input())
data=list(map(int,input().split()))
quick_sort(0,len(data)-1,data)

mid=len(data)%2

if mid==0:
    print(data[len(data)//2-1])
else:
    print(data[len(data)//2])
