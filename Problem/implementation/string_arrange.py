"""
문자열 재정렬 문제 (facebook 인터뷰)
알파벨 대문자와 0~9로 이루어진 문자열이 주어질 때 문자열 먼저 오름차순 그 뒤에 숫자를 더한 값을 출력하는 문제이다.
"""

ss=input()
a=[]
b=0
for i in ss:
    if i.isalpha():
        a.append(i)
    else:
        b+=int(i)

a.sort()

for j in a:
    print(j,end='')
print(b)
        