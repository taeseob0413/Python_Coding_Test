"""
부분배낭 문제
무게 제한이 K인 배낭에 최대 가치를 가지도록 물건을 넣는 문제.
물건은 쪼갤 수 있으므로 물전의 일부분이 배낭에 넣어질 수 있음. (쪼개서 넣을 수 없는 배낭문제도 존재)
물건은 무게와 가치로 표현
"""
data_list=[(10,10),(15,12),(20,10),(25,8),(30,5)]
k=int(input())
value=0
data_list.sort(key=lambda x:x[1]/x[0],reverse=True) #배낭에 담겨있는 물건을 무게당 가치가 높은 순으로 정렬을 함.

for data in data_list:
    if k==0:
        break
    if data[0]<=k:
        k=k-data[0]
        value+=data[1]
    else:
        value+=(data[1]/data[0])*k
        k=0
print(value)

"""
이 문제의 당위성은 무게당 가치순을 내림차순으로 하였을 때 물건이 쪼개질 수 있으므로 무게당 가치가 높은 물건을 담는 것이 무조건 유리하다.
"""