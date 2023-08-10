"""
떡볶이 떡 만들기 문제

N개의 떡이 존재하고 H의 높이에 맞게 N개의 떡을 자른다. 이때 잘린 부분을 손님이 갖고 갈수 있다.
이때 절단기의 최대 높이 M을 구하는 문제

>>이 문제의 경우에는 손님이 적어도 M만큼의 떡을 갖고 갈 수 있도록 하게하면서 높이 H를 최대로 해야한다는 점에서 최적화 문제라고 볼 수 있다.
>>즉 M을 만족한 순간부터 H의 높이를 늘려가면서 최대 높이 H를 찾아야 한다.
>>절단기의 높이는 0~현재 갖고 있는 떡의 최대 높이로 설정을 하면 되고 떡의 최대 높이는 10억이므로 o(log십억)의 시간복잡도로 알맞게 끝낼 수 있다.
"""

#가장 긴 절단기의 높이를 저장하는 변수
high_h=0

def binary_search_while(data,start,end,target):
    while start<=end:
        global high_h

        #절단기의 범위 0~현재 갖고 있는 떡의 최대 높이
        mid=(start+end)//2

        #잘린 떡들의 합을 저장하기 위한 변수
        sum=0

        #갖고 있는 떡들 중에서 절단기의 높이보다 긴 떡들을 잘라 합을 구하는 과정
        for i in data:
            if i>mid:
                sum+=(i-mid)

        #합이 손님이 원하는 떡의 길이 보다 긴 경우 절단기의 높이를 높이는 과정
        if sum>=target:
            high_h=mid
            start=mid+1
        else:
            end=mid-1


n,m=map(int,input().split())
data=list(map(int,input().split()))
binary_search_while(data,0,max(data),m)
print(high_h)

#총 시간 복잡도는 O(Nlog십억)