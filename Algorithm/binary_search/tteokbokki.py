"""
떡볶이 떡 만들기!!
N개의 떡과 그 높이들이 주어지고 손님이 원하는 떡의 높이는 M으로 주어질 때
떡을 자르는 높이를 설정하여 손님이 원하는 떡의 높이를 제공할 수 있는 최대 떡의 높이를 구하는 문제

>>파라메트릭 서치 유형의 문제(최적화 문제를 결정 문제로 바꾸어 해결하는 기법)
문제의 제한시간은 2초 = 4000만번의 연산
O(NlogN)의 시간 복잡도로 풀 경우 3000만번의 연산(떡의 높이 10억 == log10억 == 31 / N=100만)으로 아슬아슬하게 시간 제한 통과 가능

"""
def binary_search(start,end,target,array):
    global result
    if start>end:
        return
    mid=(start+end)//2
    sum=0
    for i in range(len(array)):
        if array[i]>mid:
            sum+=(array[i]-mid)
    if sum>=target:
        result=mid
        return binary_search(mid+1,end,target,array)
    else:
        return binary_search(start,mid-1,target,array)


n,m=map(int,input().split())
tteok_list=list(map(int,input().split()))
tteok_list.sort()
result=0
binary_search(0,tteok_list[-1],m,tteok_list)
print(result)
