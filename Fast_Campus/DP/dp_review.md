### 다이나믹 프로그래밍

- DP는 최적의 해를 구하는 문제에서 메모리 공간을 사용하여 연산 속도를 높이는 알고리즘
- 탑다운 & 보텀업 방식이 존재하고 메모이제이션 기법을 사용

Memoization : 한 번의 구현결과를 메모리 공간에 저장 후 같은 식이 도출될 시 메모한 결과를 갖고 오는 기법

- 한 예로 피보나치 수열을 들 수 있음.

피보나치 수열의 경우에 재귀함수로 구현할 경우 O(2^N)의 시간복잡도를 갖지만 DP로 구현할 시 O(N)의 시간복잡도를 갖음

```python : fibo.py

#재귀 함수를 이용한 fibo
def fibo(n):
    if n<=2:
        return 1
    return fibo(n-1)+fibo(n-2)

#dp 탑다운
dp=[0]*(101)
def dp_top_down(n):
    if n<=2:
        return 1
    if dp[n]!=0:
        return dp[n]
    dp[n]=dp_top_down(n-1)+dp_top_down(n-2)
    return dp[n]

#dp 보텀업
dp1=[0]*(101)
dp1[1],dp[2]=1,1
n=99
for i in range(3,n+1):
    dp1[i]=dp1[i-1]+dp1[i-2]

prinit(fibo(99),dp_top_down(99),dp1[99])
```