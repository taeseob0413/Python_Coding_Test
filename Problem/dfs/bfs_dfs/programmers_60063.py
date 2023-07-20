"""
블록 이동하기 문제
1x2크기의 로봇이 존재하고 N,N의 지점까지 가길 원할 때 최소시간 구하는 문제

>>이 문제는 로봇이 1x2크기 또는 2x1크기로 회전하면서 진행을 할 수 있고 회전할 때 1초가 걸린다는 점에서 어려운 문제
>>최소시간으로 가기 위해서는 로봇이 회전을 할 때 아래쪽 or 오른쪽으로 회전을 해야한다.
"""
from collections import deque
def solution(board):
    #로봇의 상태 0 >> 가로 누워있는 상태 / 1>> 세로 누워있는 상태
    answer = 0

    q=deque()
    q.append(((0,0),(0,1),0,0))
    board[0][0],board[0][1]=2,2

    n=len(board)
    while q:
        l1,l2,dir,time=q.popleft()
        x1,y1=l1
        x2,y2=l2

        if (x1==n-1 and y1==n-1) or (x2==n-1 and y2==n-1):
            answer=time
            break

        if dir==0:
            if y2+1<len(board):
                if board[x2][y2+1]==0:
                    board[x2][y2+1]=2
                    q.append(((x2,y2),(x2,y2+1),0,time+1))
            if x2+1<len(board) and board[x2+1][y1]==0:
                if board[x2+1][y2]==0:
                    board[x2+1][y2]=2
                    q.append(((x2,y2),(x2+1,y2),1,time+1))
            if x2-1>=0 and board[x2-1][y1]==0:
                if board[x2-1][y2]==0:
                    board[x2-1][y2]=2
                    q.append(((x2-1,y2),(x2,y2),1,time+1))

        elif dir==1:
            if x2+1<len(board):
                if board[x2+1][y2]==0:
                    board[x2+1][y2]=2
                    q.append(((x2,y2),(x2+1,y2),1,time+1))
            if y1+1<len(board) and board[x1][y1+1]==0:
                if board[x2][y2+1]==0:
                    board[x2][y2+1]=2
                    q.append(((x2,y2),(x2,y2+1),0,time+1))
            if y1-1<len(board) and board[x1][y1-1]==0:
                if board[x2][y2-1]==0:
                    board[x2][y2-1]=2
                    q.append(((x2,y2-1),(x2,y2),0,time+1))
    return answer

board=[[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]

print(solution(board))