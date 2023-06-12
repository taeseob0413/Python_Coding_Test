"""
개미 전사문제

개미 전사는 메뚜기의 식량창고를 습격하여 최대한 많은 식량을 약탈하고자 한다.(이때 연속한 두 개의 창고를 공격할 수는 없음)

이 문제 역시 dp로 풀면 쉽게 풀 수 있는 문제
어떤 n번째 창고를 털기 위해서는 n-2번째와 n-3번째 창고중 많은 수의 식량과 본인의 식량을 합치면 된다.
이후 d 리스트에서 가장 큰 값을 출력
"""

n=int(input())
d=[0]*(100)
food_list=list(map(int,input().split()))
d[0]=food_list[0]
d[1]=food_list[1]
d[2]=food_list[2]+d[0]
d[3]+=food_list[3]+d[1]
if n>=5:
    for i in range(4,n):
        d[i]=food_list[i]+max(d[i-2],d[i-3])
print(max(d))

#해설지 풀이
d1=[0]*100
d1[0]=food_list[0]
d1[1]=max(food_list[0],food_list[1])
for i in range(2,n):
    d1[i]=max(d1[i-1],d1[i-2]+food_list[i])
print(d1[n-1])

#내 풀이의 경우에는 food_list[i]의 창고를 무조건 턴다는 가정으로 d[n]을 설정하였고
#해설지 풀이의 경우에는 n번째에서 얻을 수 있는 최대의 수를 가정하고 d1[n]을 설정.