"""
성적이 낮은 순서로 학생 출력하기
N이 주어지고 N명의 학생의 이름과 성적이 주어진다.(1<=N<=10만)
성적이 낮은 순서대로 출력하고 문제에서는 성적이 같을 때 자유롭게 출력하라고 되어있지만 가다나 순으로 출력을 해 볼 예정

>>N이 10만이므로 O(N^2)의 정렬 알고리즘말고 O(NlogN)의 정렬 알고리즘을 사용하여야 한다.
"""

n=int(input())
grade_list=[]
for _ in range(n):
    x,y=input().split()
    grade_list.append((x,int(y)))

grade_list.sort(key=lambda x:(x[1],x[0]))

for i in grade_list:
    print(i[0],end=' ')
