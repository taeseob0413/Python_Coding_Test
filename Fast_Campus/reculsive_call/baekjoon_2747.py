"""
재귀 호출 문제
"""
import sys

input=sys.stdin.readline
def fibo(n):
    if n<=0:
        return 0
    if n==1:
        return 1

    return fibo(n-1)+fibo(n-2)

n=int(input())
print(fibo(n))