"""
0만들기 문제

>>이 문제에서 테스트 케이스가 10개 미만이고 N이 3~9이므로
>>오름 차순으로 정렬된 수렬 1~N과 연산자 3개("+","-"," ")의 모든 가능 경우가 3**8이고 모든 테스트 케이스를 고려하면
>>10*3**8이므로 시간 제한에 상관없이 알맞게 끝낼 수 있다.
>>eval라이브러리 사용
"""
import copy

def target_zero(array,n):
    if len(array)==n:
        operations_list.append(copy.deepcopy(array))
        return

    array.append(" ")
    target_zero(array, n)
    array.pop()

    array.append("+")
    target_zero(array,n)
    array.pop()

    array.append("-")
    target_zero(array,n)
    array.pop()



test_case=int(input())

for _ in range(test_case):
    num=int(input())
    operations_list=[]

    target_zero([],num-1)

    number_list=[i for i in range(1,num+1)]

    for operators in operations_list:
        string=""
        for i in range(num-1):
            string+=str(number_list[i])+operators[i]
        string+=str(number_list[-1])

        if eval(string.replace(" ",""))==0:
            print(string)
    print()