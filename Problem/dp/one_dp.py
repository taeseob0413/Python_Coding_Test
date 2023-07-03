"""
1만들기
x가 주어질 때 5로 나누기 or 3으로 나누기 or 2로 나누기 or 1빼기 4가지의 연산이 가능하다.
x가 1이 되는 가장 작은 연산의 횟수를 구하는 문제

>>dp를 사용하게 되면 300001번의 연산안에서 해결할 수 있음.
"""
x=int(input())
num_list=[0]*(x+1)

#4가지의 연산 중에서 1을 빼는 연산으로 초기화 해놓은 상태
for i in range(1,len(num_list)):
    num_list[i]=i-1

for i in range(1,len(num_list)):
    if i*2<=x:
        num_list[i*2]=min(num_list[i*2],num_list[i]+1)
    if i*3<=x:
        num_list[i*3] = min(num_list[i*3], num_list[i] + 1)
    if i*5<=x:
        num_list[i*5] = min(num_list[i*5], num_list[i] + 1)
    if i+1<=x:
        num_list[i+1]=min(num_list[i+1],num_list[i]+1)
print(num_list[x])