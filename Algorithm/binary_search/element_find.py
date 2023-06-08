"""
부품 찾기 문제

부품 가게에 N개의 부품이 존재하고 각 부품별로 번호가 있음. (1<=N<=백만)
손님은 M개의 부품을 주문하고 주문서에는 필요한 부품의 번호가 존재한다 (1<=M<=십만)

손님이 주문한 M개의 부품이 모두 부품가게에 존재할 시 yes를 출력하고 없을 시 no를 출력하는 문제이다.


>>N이 매우 크므로 부품 가게의 부품 중에 손님이 갖고 있는 부품을 탐색할 때는 이진 탐색을 사용해야함 O(MlonN)
>>이진 탐색을 하기 위해서 사전에 정렬 작업 필요(NlogN)
>>정렬은 라이브러리 사용없시 퀵 정렬을 사용해보려고함.
"""
def quick_sort(data,start,end):
    if start>=end:
        return
    left=start+1
    right=end
    pivot=start
    while left<=right:
        while data[left]<=data[pivot] and left<=end:
            left+=1
        while data[right]>=data[pivot] and right>start:
            right-=1
        if left>right:
            data[pivot],data[right]=data[right],data[pivot]
        else:
            data[right],data[left]=data[left],data[right]
    quick_sort(data,start,right-1)
    quick_sort(data,right+1,end)

def binary_search(start,end,target,array):
    while start<=end:
        mid=(start+end)//2
        if array[mid]==target:
            return True
        elif array[mid]>target:
            end=mid-1
        else:
            start=mid+1
    return False

n=int(input())
element_list=list(map(int,input().split()))
m=int(input())
order_list=list(map(int,input().split()))
quick_sort(element_list,0,n-1)

print(element_list)
for order in order_list:
    if binary_search(0,n-1,order,element_list)==False:
        print("no")
    else:
        print("yes")


