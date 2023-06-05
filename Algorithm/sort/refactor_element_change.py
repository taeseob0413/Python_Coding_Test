"""
두 배열의 원소교체
두 배열이 주어지고 두 배열은 N개의 원소로 이루어져 있음(1<=N<=10만)
최대 K번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 모든 원소의 합의 최댓값을 출력하는 프로그램.
>>배열 A의 경우에는 오름차순 정렬을 하고 배열 B의 경우에는 내림차순 정렬을 하여 B의 가장 큰 값과 A의 가장 작은 값을 비교하여
B의 가장 큰 값 >A의 가장 작은 값일 경우 교체를 해주고 아닐 경우에는 교체를 끝냄.
"""

n,k=map(int,input().split())
num_list1=list(map(int,input().split()))
num_list2=list(map(int,input().split()))

#n이 최대 십만까지 가능하므로 정렬은 O(NlogN)의 시간복잡도를 사용해야함
num_list1.sort()
num_list2.sort(reverse=True)

for i in range(k):
    if num_list1[i]<num_list2[i]:
        num_list2[i],num_list1[i]=num_list1[i],num_list2[i]
    else:
        break
print(sum(num_list1))
