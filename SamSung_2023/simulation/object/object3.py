"""
객체 생성(리스트)
"""
class AB():
    def __init__(self,code="",score=0):
        self.code=code
        self.score=score

#5개의 객체 생성
ab=[AB() for _ in range(5)]

index=0
min_value=101
for i in range(5):
    x,y=map(str,input().split())
    num=int(y)
    ab[i].code=x
    ab[i].score=num

    if ab[i].score<min_value:
        index=i
        min_value=ab[i].score

print(ab[index].code, ab[index].score)