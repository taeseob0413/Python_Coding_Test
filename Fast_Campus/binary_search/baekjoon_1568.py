"""
백준 새 문제

N마리의 새가 있고 한 마리씩 1부터 오름차순으로 숫자를 말한다.
숫자를 말하고 난 뒤 숫자 만큼의 새가 하늘로 날아갈 때 N마리의 새가 모두 날아가는 데 걸리는 시간을 구하는 문제
이 때 말해야하는 숫자보다 적은 수의 새가 남아있다면 다시 1부터 외친다.
"""

n=int(input())

num=1
count=0

while True:

    if n<num:
        num=1
        continue
    else:
        n-=num
        num+=1
        count+=1
    #종료 조건
    if n==0:
        break

print(count)
