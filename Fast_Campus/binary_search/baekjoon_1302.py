"""
베스트 셀러 문제

오늘 팔린 N개의 책의 이름이 주어질 때 가장 많이 팔린 책의 제목을 출력하는 문제
이때 가장 많이 팔린 책이 여러권일 경우 사전순으로 하나만 출력

>>N이 1000보다 작거나 같은 자연수이므로 시간복잡도는 크게 고려하지 않아도 되고
>>주어지는 값들이 문자열이므로 딕셔너리 자료형을 사용해 보려고 함.
"""
n=int(input())
books=dict()

for _ in range(n):
    book=input()
    if book in books:
        books[book]+=1
    else:
        books[book]=1

books_list=list(books.items())
books_list.sort(key=lambda x:(-x[1],x[0]))
print(books_list[0][0])