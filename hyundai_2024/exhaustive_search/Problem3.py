n = int(input())
INF=int(1e9)
number_list = []

for i in range(n):
    number_list.append(list(map(int, input().split())))

total_sum = INF

for i in range(1, n - 1):
    tmp = number_list[:i] + number_list[i + 1:]
    sub_sum = 0
    for j in range(n - 2):
        sub_sum += abs(tmp[j][0] - tmp[j + 1][0]) + abs(tmp[j][1] - tmp[j + 1][1])
    total_sum = min(total_sum, sub_sum)

print(total_sum)
