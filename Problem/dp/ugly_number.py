"""
못생긴 수 문제
"""
n=int(input())
u=[0]*n
i1,i2,i3=0,0,0
next2,next3,next5=2,3,5

for i in range(1,n):
    u[i]=min(next2,next3,next5)

    if u[i]==next2:
        i1+=1
        next2=u[i1]*2
    if u[i]==next3:
        i2+=1
        next3=u[i2]*3
    if u[i]==next5:
        i3+=1
        next5=u[i3]*5
print(u[n-1])

