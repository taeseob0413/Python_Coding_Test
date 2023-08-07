"""
국영수 문제

정렬을 하는데 여러가지 조건이 있고 데이터의 갯수가 10만개 이므로 sort라이브러리로 해결을 하려고 한다.
특히 여러 조건이 있기 때문에 lambda식을 사용하면 문제를 해결할 수 있다.
"""
n=int(input())
student_list=[]

for _ in range(n):
    a,b,c,d=map(str,input().split())
    student_list.append((a,int(b),int(c),int(d)))

student_list.sort(key=lambda x:(-x[1],x[2],-x[3],x[0]))

for i in student_list:
    print(i[0])