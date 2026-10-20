x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
x1[2], y1[2], x2[2], y2[2] = map(int, input().split())

# Please write your code here.
answer = 0

for i in range(2):
    # 직사각형 A 또는 B의 넓이
    area = (x2[i] - x1[i]) * (y2[i] - y1[i])

    # M과 겹치는 부분의 좌표
    left = max(x1[i], x1[2])
    right = min(x2[i], x2[2])
    bottom = max(y1[i], y1[2])
    top = min(y2[i], y2[2])

    # 겹치는 부분의 넓이
    overlap = max(0, right - left) * max(0, top - bottom)

    # M으로 덮이지 않은 넓이
    answer += area - overlap

print(answer)