"""
볼링공 문제 답지 해설
내가 푼 문제에서는 시간 복잡도가 O(N^2)이었는데 답지의 풀이의 경우에는
O(N)으로 가능해서 더 빠름

답지의 아이디어는 볼링공의 무게가 가장 작은 순부터 A가 선택한다고 할 때
B가 선택할 수 있는 볼링공은 N(볼링공의 개수)-A가 선택한 공 이므로
두 개를 곱해주면 되는 문제였다.
"""
n,m=map(int,input().split())
bowling_list=list(map(int,input().split()))
bowling_w=[0]*11  #볼링공의 무게가 1~10이므로 무게에 따른 볼링공을 카운트하는 리스트
result=0
for i in bowling_list:
    bowling_w[i]+=1

for i in range(1,m+1):
    n-=bowling_w[i]
    result+=bowling_w[i]*n #bowling_w[i]는 A가 선택하는 경우 n은 B가 선택하는 경우
print(result)