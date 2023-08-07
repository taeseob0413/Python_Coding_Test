"""
카드 정렬하기 문제

이 문제의 경우에는 현재 갖고 있는 카드 중에서 가장 작은 두개를 뽑아서 합쳐서 한 카드로 만드는 과정을 반복하는 문제이다.
이때 만약 매 단계마다 sort함수를 구현하게 되면 시간초과 or 출력초과가 발생하게 된다.
하지만 heapq를 활용하면 N번의 삽입 삭제에서 O(NlogN)의 시간복잡도로 문제를 해결할 수 있으므로 데이터의 갯수가 10만개 이하인 이번 문제를
해결하는 데 어려움이 없다.
"""
import heapq

n=int(input())

card_list=[]

for _ in range(n):
    heapq.heappush(card_list,int(input()))
sum=0
while True:
    if len(card_list)<=1:
        break
    a=heapq.heappop(card_list)
    b=heapq.heappop(card_list)
    sum+=a+b
    heapq.heappush(card_list,(a+b))

print(sum)