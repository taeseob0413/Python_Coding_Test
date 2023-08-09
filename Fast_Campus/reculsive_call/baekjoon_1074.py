"""
Z문제
"""

count=0

def z_function(n,r,c):
    global count
    if n==1:
        if r==0 and c==0:
            count+=0
        elif r==0 and c==1:
            count+=1
        elif r==1 and c==0:
            count+=2
        else:
            count+=3
        return

    #1번 영역
    if 0<=r<2**(n-1) and 0<=c<2**(n-1):
        return z_function(n-1,r,c)

    #2번 영역
    if 0 <= r < 2**(n - 1) and 2**(n - 1) <= c < 2**n:
        count+=2**(2*n-2)
        return z_function(n - 1, r, c-2**(n-1))

    #3번 영역
    if 2**(n-1)<=r<2**n and 0<=c<2**(n-1):
        count+=2*2**(2*n-2)
        return z_function(n-1,r-2**(n-1),c)

    #4번 영역
    if 2**(n-1)<=r<2**n and 2**(n - 1) <= c < 2**n:
        count+=3*2**(2*n-2)
        return z_function(n-1,r-2**(n-1),c-2**(n-1))

n,r,c=map(int,input().split())
z_function(n,r,c)
print(count)
