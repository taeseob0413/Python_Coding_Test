"""
카드 정렬하기 >>atm과 같이 누적합 문제
"""
#출력 초과 발생 코드
n=int(input())
num_list=[]
for _ in range(n):
    num_list.append(int(input()))
num_list.sort()

if len(num_list)==1:
    print(num_list[0])
else:
    sum=num_list[0]+num_list[1]
    for i in range(2,len(num_list)):
        sum+=sum+num_list[i]
    print(sum)
#문제 이해를 잘못하였음 >> 매번 카드를 비교할 때 현재 존재하는 카드 중에서 가장 작은 2개를 선택하는 경우이다.
#이 경우에 매번 N번 동안 NlogN의 정렬을 사용하면 시간초과가 발생하기 때문에 heapq를 사용하여야 한다.