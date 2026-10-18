n = int(input())

A = [[0] * 201 for _ in range(201)]

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(x1, x2):
        for j in range(y1, y2):
            A[i + 100][j + 100] = 1

answer = 0

for i in range(201):
    for j in range(201):
        if A[i][j] == 1:
            answer += 1

print(answer)