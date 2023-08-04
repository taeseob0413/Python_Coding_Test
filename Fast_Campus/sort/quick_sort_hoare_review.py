"""
퀵 정렬(hoare)
"""
import random

def quick_sort_hoare(start,end,data):
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

    quick_sort_hoare(start,right-1,data)
    quick_sort_hoare(right+1,end,data)

num_list=random.sample(range(100),50)
print(num_list)
quick_sort_hoare(0,len(num_list)-1,num_list)
print(num_list)