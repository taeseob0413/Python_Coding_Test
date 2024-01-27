"""
조건에 따라 방향이 변하는 경우

n * n 크기의 격자 위 (x, y) 위치에서 공이 상하좌우 중 한 방향으로 이동중입니다.
이동 도중 격자 끝에 다다르면, 방향을 반대로 바꿔 다시 움직입니다.
1초에 한 칸씩 움직인다 했을 때, 10초 뒤 공의 위치는 어떻게 되나요?
"""

n = 5
x, y = 1, 2
dir_num = 2

dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n



nx, ny = x + dxs[dir_num], y + dys[dir_num]
if not in_range(nx, ny):  # check whether position is out of grid
    dir_num = 3 - dir_num  # change direction

# move
x, y = x + dxs[dir_num], y + dys[dir_num]

#방향이 문자열로 주어졌을 때
mapper = {
    'R': 0,
    'D': 1,
    'U': 2,
    'L': 3
}

