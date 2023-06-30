"""
카드 정렬하기 >>atm과 같이 누적합 문제
"""
#출력 초과 발생 코드
n=int(input())
num_list=[]
for _ in range(n):
    num_list.append(int(input()))
num_list.sort()

if len(num_list)==1:
    print(num_list[0])
else:
    sum=num_list[0]+num_list[1]
    for i in range(2,len(num_list)):
        sum+=sum+num_list[i]
    print(sum)