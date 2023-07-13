"""
문자열 뒤집기

길이 백만 이하의 문자열이 0과 1의 형태로 주어진다.
이때 가장 적게 숫자를 뒤집어서 한가지의 문자열로 만드는 문제.

>>이 문제의 경우에는 그리디 알고리즘으로 풀 수 있다.
>>문제의 아이디어는 맨 처음나오는 문자와 다른 연속된 문자들을 뒤집어주면 된다.
>>O(n)의 시간복잡도로 풀 수 있음.
"""

n=input()
start=n[0]

#문자열의 연속을 체크하기위한 flag
flag=False
count=0
for i in range(1,len(n)):
    if start!=n[i] and flag==False:
        count+=1
        flag=True
    elif start==n[i] and flag==True:
        flag=False

print(count)



