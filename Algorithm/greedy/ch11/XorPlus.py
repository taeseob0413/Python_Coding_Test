"""
곱하거나 더하거나
길이가 1<= <=20인 문자열이 주어지고 왼쪽부터 읽어가면서 곱하거나 더하는 연산을 할 때 가장 큰 경우를 찾아야함.
단 계산은 더하거나 곱하는 계산의 우선순위는 왼쪽에 있는 게 우선순위가 높음

이 문제는 읽어가면서 만약 더하거나 곱하는 두 수가 0 or 1 일 때는 더하기 연산을 해주고 나머지는 곱하기를 해주면 됨.
"""
num=input()
total=int(num[0])
plus_set={0,1}
for i in range(1,len(num)):
    if total in plus_set or num[i] in plus_set:
        total+=int(num[i])
    else:
        total*=int(num[i])
print(total)
