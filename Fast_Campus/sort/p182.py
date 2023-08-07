"""
p182 두 배열의 원소교체 문제
A,B 배열이 존재할 때 최대 K번의 원소를 교환할 수 있다. 이때 A배열의 원소들의 합이 최대가 되도록 하는 문제.

>>이 문제의 경우에는 배열 A는 오름차순 배열 B는 내림차순으로 정렬을 한 뒤 같은 위치의 원소를 비교하여 B의 원소가 더 큰 경우에는 교체를 해주면 된다.
"""

n,k=map(int,input().split())
list_a=list(map(int,input().split()))
list_b=list(map(int,input().split()))

list_a.sort()
list_b.sort(reverse=True)

for i in range(k):
    if list_a[i]<list_b[i]:
        list_b[i],list_a[i]=list_a[i],list_b[i]
    else:
        break

sum=0
for i in range(n):
    sum+=list_a[i]
print(sum)
