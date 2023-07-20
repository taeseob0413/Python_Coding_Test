"""
카드 정렬하기
매번 가장 작은 2개를 뽑아야 하는 문제이다.
이떄 N-1번의 단계가 필요한데 이때마다 정렬을 수행하게 되면
O(N*N*logN)의 시간복잡도가 필요하기 떄문에 시간초과에 걸린다.
대신 heap정렬을 이용하면 매 N-1번의 단계에서 삽입/삭제가 O(logN)이므로 총 시간 복잡도는 O(NlogN)이 발생하는 것을 알 수 있다.
"""
import heapq
n=int(input())
num_list=[]
for _ in range(n):
    heapq.heappush(num_list,int(input()))

sum=0
while len(num_list)>=2:
    a=heapq.heappop(num_list)
    b=heapq.heappop(num_list)
    sum+=a+b
    heapq.heappush(num_list,a+b)

print(sum)
