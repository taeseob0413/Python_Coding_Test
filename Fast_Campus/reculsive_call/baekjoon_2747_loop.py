"""
피보나치 수열을 while문을 통해 구현
"""

n=int(input())
count=2
a,b=0,1
while count<=n:
    a,b=b,a+b
    count+=1
print(b)