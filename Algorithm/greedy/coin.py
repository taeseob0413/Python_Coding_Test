"""
동전 계산 문제
500,100,50,10원의 동전이 존재할 때 금액을 입력받고 이를 제공할 수 있는 최소한의 동전개수를 찾는 문제.
단) 동전은 모두 10의 배수
"""
coin_list=[500,100,50,10]
n=int(input())
count=0
for coin in coin_list:
    count+=n//coin
    n=n%coin
print(count)

"""
시간 복잡도는 주어진 금액과 무관하고 동전의 종류에 따라서 달라지므로 O(K)이다.
그리디의 정당성 : 주어진 동전의 타입에서 큰 동전은 항상 작은 동전의 배수이다. 즉 이말은 가지고 있는 동전 중에서 큰 단위가 항상 작은 단위의 배수이므로
작은 단위의 동전들을 종합하여 다른 해가 나올 수 없다는 것을 뜻한다.
실제로 거스름돈 문제에서 동전(화폐)의 단위가 서로 배수 형태가 아니라, 무작위로 주어진 경우에는 그리디 알고리즘으로 문제 해결하지 못함.
>>다이나믹 프로그래밍으로 해결!!
"""