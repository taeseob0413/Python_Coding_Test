"""
N자리 2진수 만들기
"""
answer=[]

n=int(input())

def print_answer():
    for i in answer:
        print(i,end=" ")
    print()
    return
def choose(cur_num):
    if cur_num==n+1:
        print_answer()
        return

    answer.append(0)
    choose(cur_num+1)
    answer.pop()

    answer.append(1)
    choose(cur_num + 1)
    answer.pop()

    return

choose(1)