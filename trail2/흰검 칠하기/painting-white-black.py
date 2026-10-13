n = int(input())
commands = [tuple(input().split()) for _ in range(n)]

MAX = 200000
OFFSET = 100000

white_cnt = [0] * MAX
black_cnt = [0] * MAX
color = [0] * MAX
# 0: 아직 안 칠함
# 1: 흰색
# 2: 검은색
# 3: 회색

pos = OFFSET

for x, direction in commands:
    x = int(x)

    if direction == 'L':
        for i in range(x):
            idx = pos - i

            # 이미 회색이면 더 이상 바뀌지 않음
            if color[idx] == 3:
                continue

            white_cnt[idx] += 1

            if white_cnt[idx] >= 2 and black_cnt[idx] >= 2:
                color[idx] = 3
            else:
                color[idx] = 1

        # 마지막으로 칠한 위치
        pos -= x - 1

    else:  # R
        for i in range(x):
            idx = pos + i

            if color[idx] == 3:
                continue

            black_cnt[idx] += 1

            if white_cnt[idx] >= 2 and black_cnt[idx] >= 2:
                color[idx] = 3
            else:
                color[idx] = 2

        pos += x - 1

white = color.count(1)
black = color.count(2)
gray = color.count(3)

print(white, black, gray)