n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

A = [0 for _ in range(200)]

for x1, x2 in segments:
    x1 += 100
    x2 += 100
    for i in range(x1, x2):
        A[i] += 1

print(max(A))