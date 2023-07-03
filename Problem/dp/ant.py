"""
개미전사 문제
"""
n=int(input())
food_list=list(map(int,input().split()))

food_list[2]+=food_list[0]
for i in range(3,len(food_list)):
    food_list[i]=max(food_list[i-2],food_list[i-3])+food_list[i]
print(max(food_list))

#해설지 풀이
d1=[0]*100
d1[0]=food_list[0]
d1[1]=max(food_list[0],food_list[1])
for i in range(2,n):
    d1[i]=max(d1[i-1],d1[i-2]+food_list[i])
print(d1[n-1])

#내 풀이의 경우에는 food_list[i]의 창고를 무조건 턴다는 가정으로 d[n]을 설정하였고
#해설지 풀이의 경우에는 n번째에서 얻을 수 있는 최대의 수를 가정하고 d1[n]을 설정.