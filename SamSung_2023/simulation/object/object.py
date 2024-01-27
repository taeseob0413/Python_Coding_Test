"""
객체 생성
"""
class Student:
    #객체 생성자
    def __init__(self,kor,eng,math):
        self.kor=kor
        self.eng=eng
        self.math=math

stu=Student(10,20,30)
