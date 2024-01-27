string = "banana"
arr = list(string)
arr.sort()
print(arr) # ['a', 'a', 'a', 'b', 'n', 'n']
sorted_str = ''.join(arr)
print(sorted_str) # aaabnn


#문자열 비교하기
def starts_with(a, b):
    # b의 길이가 더 길 수는 없습니다.
    if len(a) < len(b):
        return False

    # b의 길이만큼 살펴보며, a와 문자열이 완벽히 동일한지 확인합니다.
    return a[:len(b)] == b