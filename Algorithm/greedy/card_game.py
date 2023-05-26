"""
이코테 숫자 카드게임
NxM의 형태로 카드가 나열되어 있음.
하나의 행을 정하고 그 행에 있는 수중에서 가장 작은 수를 고르는 작업을 진행할 때 최종적으로 가장 큰 수가 선택되도록 하는 문제
>>즉 각행의 최소값중에서 가장 큰 수를 뽑는 문제이다.
1<N,M<=100
각 숫자는 1~10000의 자연수
"""
n,m=map(int,input().split())
max_value=0 #입력받을 수 있는 최소 자연수가 1인 것을 고려
for _ in range(n):
    num_list=list(map(int,input().split()))
    num_list.sort()
    if max_value<num_list[0]:
        max_value=num_list[0]
print(max_value)

"""
위의 시간복잡도는 O(NMlogM)인데 N,M이 각각 100이하이므로 가능하다.
"""