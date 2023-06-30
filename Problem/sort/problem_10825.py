"""
국영수 문제

학생 N명이 주어지고 이름 국어점수 수학점수 영어점수가 주어질 때
1국어 점수가 감소하는 순 2 국어 점수가 같을 때 영어 점수가 증가하는 순 3 국어 영어점수가 같으면 수학 점수가 감소하는 순서로 4 모든 점수가 같을 때
이름이 사전순으로 증가하는 형태로 출력하기

N이 10만 이하이므로 정렬 라이브러리를 사용하면 O(NlogN)의 시간 복잡도 안에 끝낼 수 있다.
"""

n=int(input())
stu_list=[]
for _ in range(n):
    a,b,c,d=map(str,input().split())
    stu_list.append([a,int(b),int(c),int(d)])


stu_list.sort(key=lambda x:(-x[1],x[2],-x[3],x[0]))
for i in stu_list:
    print(i[0])
