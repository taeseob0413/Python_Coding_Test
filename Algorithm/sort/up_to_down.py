"""
위에서 아래로 문제
첫째 줄에 N이 주어지고 그 뒤로 N개의 숫자가 주어질 때 내림차순 정렬하기!
N=500이므로 어떤 정렬을 사용해도 됨.
연습할 겸 퀵 정렬 알고리즘으로 풀기  >> 해답에서는 sort함수 사용
"""
n=int(input())
num_list=[]
for _ in range(n):
    num_list.append(int(input()))

def quick_sort(start,end,data):
    #데이터의 개수가 1개일 경우 종료
    if start>=end:
        return
    pivot=start
    left=start+1
    right=end

    while left<=right:
        while left<=end and data[pivot]>=data[left]:
            left+=1
        while right>start and data[pivot]<=data[right]:
            right-=1
        if left>right:
            data[pivot],data[right]=data[right],data[pivot]
        else:
            data[left],data[right]=data[right],data[left]
    quick_sort(start,right-1,data)
    quick_sort(right+1,end,data)

quick_sort(0,n-1,num_list)
num_list.reverse()
for i in num_list:
    print(i)