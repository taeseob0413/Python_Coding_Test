"""
퀵 정렬을 호어 분할 방식으로 구현한 것
맨 앞의 값을 pivot으로 정한다.
pivot의 바로 옆부터 pivot보다 큰 값을 구하고 데이터의 맨 뒤부터 pivot보다 작은 값을 구한다.
만약 두 값이 엇갈렸을 경우 작은 값과 pivot을 교체
엇갈리지 않았을 경우에는 큰 값과 작은 값을 교체하는 알고리즘.
"""
import random
def quick_sort(start,end,data):
    #원소의 개수가 1개일 경우에는 종료
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
            data[pivot],data[right]=data[right],data[pivot]
        else:
            data[left],data[right]=data[right],data[left]
    quick_sort(start,right-1,data)
    quick_sort(right+1,end,data)

data_list=random.sample(range(100),50)
quick_sort(0,len(data_list)-1,data_list)
print(data_list)
