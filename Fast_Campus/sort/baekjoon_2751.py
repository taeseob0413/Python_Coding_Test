"""
수 정렬하기2

>>데이터의 갯수가 백만개 이므로 O(N^2)인 버블,선택,삽입 정렬로는 푸는 것이 어려움
>>O(NlogN)의 정렬 라이브러리, 퀵 정렬, 병합 정렬이 필요 / O(10^6 * log 2^20) >> O(2천만)
>>병합 정렬로 풀어보기
"""
import sys

input=sys.stdin.readline

n=int(input())
num_list=[int(input()) for _ in range(n)]

def merge(left,right):
    lp,rp=0,0
    result=[]

    while lp<len(left) and rp<len(right):
        if left[lp]<right[rp]:
            result.append(left[lp])
            lp+=1
        else:
            result.append(right[rp])
            rp += 1

    while lp<len(left):
        result.append(left[lp])
        lp+=1

    while rp<len(right):
        result.append(right[rp])
        rp+=1
    return result

def merge_split(data):
    if len(data)<=1:
        return data

    mid=len(data)//2

    left=merge_split(data[:mid])
    right=merge_split(data[mid:])

    return merge(left,right)

result=merge_split(num_list)
for i in result:
    print(i)