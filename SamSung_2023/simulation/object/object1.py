"""
객체 생성 문제 1
"""
class Subject:
    def __init__(self,se,me,ti):
        self.se=se
        self.me=me
        self.ti=ti

a,b,c=map(str,input().split())
sb=Subject(a,b,c)

print("secret code : "+sb.se)
print("meeting point : "+sb.me)
print("time : "+sb.ti)