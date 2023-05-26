"""
이코테 큰 수의 법칙
다양한 수의 배열이 주어질 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 문제
단 같은 값이 K번을 초과하여 더해질 수 없음.
2<=N<=1000 / 1<=M<=10000 / 1<=k<=10000

이 문제의 경우에는 주어진 수를 내림차순 정렬하여 가장 큰 수를 K번 더하고 두번째로 큰 수를 한번 더하고 다시 큰 수를 M번 더하는 형식으로 가면 된다.
"""
n,m,k=map(int,input().split())
num_list=list(map(int,input().split()))
num_list.sort(reverse=True)   #O(NlogN)소요

#걸리는 시간을 줄이기 위하여 k+1개의 한쌍으로 묶어서 계산

total=0
total+=(m//(k+1))*(num_list[0]*k+num_list[1])
m=m%(k+1)
total+=m*num_list[0]

print(total)
