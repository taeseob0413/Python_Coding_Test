"""
백준 2750번 수 정렬하기 문제

입력받은 수를 정렬하려 출력하는 문제 , 데이터의 갯수가 1000개 이하이므로 어떤 정렬을 사용하여도 된다.
퀵 정렬을 사용하여 구현해볼 예정.
"""
def quick_sort(start,end,data):
    if start>end:
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
num_list=[]
for _ in range(n):
    num_list.append(int(input()))
quick_sort(0,n-1,num_list)
for i in num_list:
    print(i)