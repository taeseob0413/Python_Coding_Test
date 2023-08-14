"""
공유기 문제

>>여러번 풀었어서 쉽게 요점만 정리하고 넘어가려고 함.
>>대표적인 파라메트릭 서치 문제
>>N개의 집이 존재하고 가장 인접한 두 집사이의 최대거리를 출력하는 문제
"""
import sys

input=sys.stdin.readline
n,m=map(int,input().split())
home=[]
for _ in range(n):
    home.append(int(input()))

home.sort()
start=1
end=home[-1]-home[0]
result=0
while start<=end:
    mid=(start+end)//2
    count=1
    index=0
    for i in range(1,n):
        if home[i]-home[index]>=mid:
            count+=1
            index=i
            if count>=m:
                start=mid+1
                result=mid
                break
    if count<m:
        end=mid-1
print(result)