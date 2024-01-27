"""
객체 생성 및 값 변경
"""

class Student():
    #이렇게 지정해주면 kor,eng,math의 값이 들어오지 않을 경우 0,0,0의 기본 값을 사용한다.
    def __init__(self,kor=0,eng=0,math=0):
        self.kor=kor
        self.eng=eng
        self.math=math

#문제 Next Level
class User:
    def __init__(self,id="codetree",lv=10):
        self.id=id
        self.lv=lv

u1=User()
a,b=map(str,input().split())
u2=User(a,int(b))

print("user "+u1.id+" lv "+str(u1.lv))
print("user "+u2.id+" lv "+str(u2.lv))