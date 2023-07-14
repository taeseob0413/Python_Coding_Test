"""
럭키 스트레이트 문제

짝수의 길이를 갖는 숫자가 주어질 때 숫자 중간을 기준으로 왼쪽 숫자의 합과 오른쪽 숫자의 합이 같을 때를 찾는 문제.
"""
num=list(map(int,input()))
mid=len(num)//2
result1=0
result2=0

for i in range(mid):
    result1+=num[i]
    result2+=num[-(i+1)]
if result1==result2:
    print("LUCKY")
else:
    print("READY")