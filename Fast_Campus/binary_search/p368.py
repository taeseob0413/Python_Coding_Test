"""
고정점 찾기 문제

고정점은 인덱스와 값이 동일한 원소를 의미함.
서로 다른 N개의 숫자가 있을 때 고정점을 출력하는 프로그램 작성하기.
고정점은 최대 1개만 존재하고, 고정점이 없을 경우에는 -1을 출력하는 문제

>>이 문제의 시간 복잡도는 O(logN)으로 정해져 있고 원소들 또한 정렬이 된 채로 주어지기 때문에 이진 탐색을 활용할 수 있다.
>>끝내는 조건은 start가 end보다 크거나 인덱스 번호와 값이 같은 경우를 찾는 것임.
>>만약 값이 인덱스의 번호보다 크다면 해당 값의 오른쪽의 원소들은 전부 인덱스의 번호보다 클 수 밖에 없으므로 왼쪽의 원소들을 탐색해야 한다.
>>만약 값이 인덱스의 번호보다 작다면 해당 값의 왼쪽의 원소들은 전부 인덱스의 번호보다 작을 수 밖에 없으므로 오른쪽의 원소들을 탐색해야 한다.
"""
#이진 탐색을 이용하여 구하기

def fixde_point(data,start,end):
    if start>end:
        return False

    mid=(start+end)//2

    if mid==data[mid]:
        return mid
    elif mid>data[mid]:
        return fixde_point(data,mid+1,end)
    else:
        return fixde_point(data,start,mid-1)

n=int(input())
num_list=list(map(int,input().split()))

result=fixde_point(num_list,0,n-1)

if result==False:
    print(-1)
else:
    print(result)
