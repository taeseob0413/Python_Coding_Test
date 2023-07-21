"""
떡볶이 떡 만들기 문제

N개의 떡이 주어지고 떡을 자를 높이 H를 정할 때 잘려진 떡의 합이 최소 M이 되도록 만드는 최대 높이 H를 찾는 문제이다.
N 100만이하 / M 2*10^9이하

>>이 문제의 경우에는 O(NlogM)으로 풀 경우에 log2*10^9 = log2*2^30 = log 2^31이므로
>>3100만번의 연산으로 풀 수 있으므로 시간 초과에 걸리지 않는다.
>>목표 M에 딱 맞게 떨어지지 않을 수도 있다는 점을 고려해야하는 문제.

cf) 파라메트릭 서치 유형의 문제 >> 범위 내에서 조건을 만족하는 가장 큰 값을 찾는 문제
"""
import sys
n,m=map(int,input().split())
ddeok=list(map(int,input().split()))
max_num=0
def binary_search(start,end,target):
    global max_num
    while start<=end:
        mid=(start+end)//2
        sum=0
        for i in ddeok:
            if i>=mid:
                sum+=i-mid
        if sum>=target:
            start=mid+1
            max_num=mid
        else:
            end=mid-1

binary_search(0,max(ddeok),m)
print(max_num)