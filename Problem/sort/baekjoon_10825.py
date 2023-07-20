"""
국영수 문제
"""

n=int(input())
score=[]

for _ in range(n):
    a,b,c,d=map(str,input().split())
    score.append((a,int(b),int(c),int(d)))

score.sort(key=lambda x:(-x[1],x[2],-x[3],x[0]))
for i in score:
    print(i[0])
