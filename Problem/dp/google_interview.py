"""
구글 인터뷰 문제

못생긴 수 : 오직 2,3,5만을 소인수로 갖는 수를 의미한다.
ex) 1,2,3,4,5,6,...... 이때 n번째 못생긴 수를 찾는 문제 (n은 1000이하)
"""

import heapq

n=int(input())

num_list=[]
count=1

heapq.heappush(num_list,2)
heapq.heappush(num_list,3)
heapq.heappush(num_list,5)
b=0
while count<n:
    b=heapq.heappop(num_list)
    count += 1
    if b*2 not in num_list:
        heapq.heappush(num_list,b*2)
    if b * 3 not in num_list:
        heapq.heappush(num_list,b*3)
    if b * 5 not in num_list:
        heapq.heappush(num_list,b*5)
print(b)