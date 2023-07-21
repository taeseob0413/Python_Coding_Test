"""
공유기 설치 문제

집의 갯수 N개와 공유기의 갯수 C개가 주어질 때 가장 인접한 두 집 사이의 거리를 최대로 만드는 문제.
N은 2십만 이하 / 집의 좌표는 10억 이하

>>O(Nlog집의 좌표 차이)>> 2*10^6 * log 2^30 >> 6000천만번의 연산을 통해 해결 가능.
>>파라메트릭 서치 문제
"""
import sys

input=sys.stdin.readline
n,c=map(int,input().split())
house=[]
for _ in range(n):
    house.append(int(input()))

#오름차순으로 정렬
house.sort()

start=1
end=house[-1]-house[0]
result=0
while start<=end:
    count=1
    mid=(start+end)//2
    index=0
    for i in range(len(house)):
        if house[i]-house[index]>=mid:
            count+=1
            index=i
        if count>=c:
            break
    if count==c:
        result=mid
        start=mid+1
    elif count>c:
        start=mid+1
    else:
        end=mid-1
print(result)

