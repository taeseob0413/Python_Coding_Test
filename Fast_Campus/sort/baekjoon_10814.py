"""
나이순 정렬 문제

나이순으로 정렬한 뒤 나이가 같을 시 먼저 입력받은 순으로 정렬을 하는 문제
"""
n=int(input())
stu_list=[]

for i in range(n):
    a,b=map(str,input().split())
    stu_list.append((int(a),b,i))

stu_list.sort(key=lambda x:(x[0],x[2]))

for i in stu_list:
    print(i[0], i[1])
