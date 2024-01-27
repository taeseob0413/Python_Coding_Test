class Student:
    def __init__(self, kor, eng, math):
        self.kor = kor
        self.eng = eng
        self.math = math

students = [
    Student(90, 80, 90), # 첫 번째 학생
    Student(20, 80, 80), # 두 번째 학생
    Student(90, 30, 60), # 세 번째 학생
    Student(60, 10, 50), # 네 번째 학생
    Student(80, 20, 10), # 다섯 번째 학생
]

students.sort(key=lambda x: -x.kor) # 국어 점수 기준 내림차순 정렬
students.sort(key=lambda x: x.kor) # 국어 점수 기준 오름차순 정렬

for student in students: # 정렬 이후의 결과 출력
    print(student.kor, student.eng, student.math)

""" 90 80 90
   90 30 60
   80 20 10
   60 10 50
   20 80 80"""

#객체에서 정렬시 합을 기준으로 정렬

class Student:
    def __init__(self, kor, eng, math):
        self.kor = kor
        self.eng = eng
        self.math = math

students = [
    Student(90, 80, 90), # 첫 번째 학생
    Student(20, 80, 80), # 두 번째 학생
    Student(90, 30, 60), # 세 번째 학생
    Student(60, 10, 50), # 네 번째 학생
    Student(80, 20, 10), # 다섯 번째 학생
]

# 점수의 총합 기준 오름차순
students.sort(key=lambda x: x.kor + x.eng + x.math)

for student in students: # 정렬 이후의 결과 출력
    print(student.kor, student.eng, student.math)