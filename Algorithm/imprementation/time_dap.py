"""
시간 문제의 해설 소스코드
3중 for문을 이용하여 완전 탐색으로 구현
"""

n=int(input())
count=0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                count+=1

print(count)