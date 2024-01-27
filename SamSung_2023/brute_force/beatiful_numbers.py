"""
아름다운 수
"""
n=int(input())

answer=[]
def check_answer():
    counting=1
    if len(answer)==1:
        if answer[0]!=1:
            return False
    for i in range(1,len(answer)):
        if answer[i-1]!=answer[i]:
            if counting%answer[i-1]==0:
                counting+=1
            else:
                return False
    return True

result=0
def beautiful_numbers(cur_num):
    global result

    if cur_num==n+1:
        if check_answer():
            print(answer)
            result+=1
        return

    for i in range(1,5):
        answer.append(i)
        beautiful_numbers(cur_num+1)
        answer.pop()
    return

beautiful_numbers(1)
print(result)
