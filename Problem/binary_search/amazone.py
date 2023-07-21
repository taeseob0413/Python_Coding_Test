"""
아마존 인터뷰

고정점 찾기 문제 >> 고정점 :인덱스 값 = 그 원소의 값 / 문제에서 O(logN)으로 설계를 해야한다고 나와있음

>>이진탐색에서 인덱스 값 mid와 그 값을 비교했을 때 원소보다 mid가 큰 경우에는 왼쪽은 볼 필요가 없음
>>원소보다 mid가 작은 경우에는 오른쪽을 볼 필요가 없음.
"""
n=int(input())
num_list=list(map(int,input().split()))

def binary_search(start,end,data):
    while start<=end:
        mid=(start+end)//2
        if data[mid]==mid:
            return mid
        elif data[mid]>mid:
            end=mid-1
        else:
            start=mid+1
    return -1


result=binary_search(0,n-1,num_list)
if result==-1:
    print(-1)
else:
    print(result)