"""
백준 문서검색 문제

>>완전 탐색으로 해결 가능 O(2500*50)이므로 시간 복잡도 충분
"""

str1=input()
str2=input()

index=0
count=0

while index<len(str1):
    if str1[index]==str2[0]:
        flag=True
        for i in range(1,len(str2)):
            if index+i < len(str1) and str1[index+i]==str2[i]:
                continue
            else:
                flag=False
                break
        if flag:
            count+=1
            index=index+len(str2)
            continue
    index+=1

#더 간결한 풀이
idx=0
result=0

while len(str1)-idx>=len(str2):
    if str1[idx:idx+len(str2)]==str2:
        result+=1
        idx+=len(str2)
    else:
        idx+=1
print(result)


print(count)