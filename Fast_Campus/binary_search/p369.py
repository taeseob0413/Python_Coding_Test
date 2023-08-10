"""
백준 공유기 설치 문제

N개의 집이 주어지고 C개의 공유기를 설치하려고 한다.
이때 가장 인접한 두 공유기 사이의 거리를 최대로 하는 문제

>>가장 인접한 두 공유기 사이의 거리를 최대로 하려면 거리를 균등하게 하여 공유기를 설치하는 것이 중요하고
>>또한 맨 처음 집에 무조건 공유기를 설치하는 것이 중요하다.
>>이때 집의 갯수가 20만개이고 집의 좌표가 0~10^9이므로 이진탐색을 활용하여야 한다.
>>공유기간의 거리는 1~가장 끝 집들간의 거리이다.
>>이 문제 역시 파라메트릭 서치 문제에 포함된다.
>>
"""

n,c=map(int,input().split())
house=[int(input()) for _ in range(n)]

#O(NlogN) >> 가능
house.sort()

start=1
end=house[-1]-house[0]

#최종 결과
max_distance=0

while start<=end:
    #현재 공유기의 갯수를 세는 변수 / 맨 처음의 집에는 설치했다고 가정하므로 count=1
    count=1

    #마지막 공유기가 설치된 장소 / 맨 처음 집에는 설치한 채로 시작했으므로 시작 인덱스는 0
    index=0

    #초기 공유기의 간격
    mid=(start+end)//2

    for i in range(1,n):
        #두 집의 거리가 현재 설정한 기준거리보다 크거나 같은 경우 count증가
        if house[i]-house[index]>=mid:
            count+=1
            index=i
            #설치된 공유기의 갯수가 만족할 경우 종료 >> 이때 간격을 늘려줘야함.
            if count>=c:
                start=mid+1
                max_distance=mid
                break

    if count<c:
        end=mid-1

#총 시간 복잡도 O(nlog10^9)  == 30*20만 OK

print(max_distance)

