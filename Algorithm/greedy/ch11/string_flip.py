"""
문자열 뒤집기
문자열 S(0과1로만 이루어짐)가 주어지고 문자열의 길이는 백만보다 작다.
이때 다솜이는 연속된 문자열을 한 번에 뒤집는 작업을 할 수 있음. 이때 가장 적은 뒤집기로 전체가 같은 문자로 이루어진 문자열 만들기.

이 문제의 경우에는 문자열의 길이가 백만이므로 O(N)의 연산만 가능하다.
문제 풀이의 핵심은 처음 문자와 다른 문자가 나올 경우 연속해서 뒤집어야 한다는 것.
ex) 11100 / 111001 / 1110010 / 111001011 이 경우 모두 첫번째 문자인 1과는 다른 0을 연속으로 뒤집어야 한다.
또한 연속됨을 알기위해서 flag를 사용하여야 한다.
"""
s=input()
check=s[0]
flag=False
total=0
for i in range(1,len(s)):
    if s[i]!=check and flag==False:
        total+=1
        flag=True
    elif s[i]==check and flag==True:
        flag=False
print(total)