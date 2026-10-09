n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

A = [0 for _ in range(100)]
for x1, x2 in segments:
    for i in range(x1-1, x2):
        A[i] += 1

print(max(A))
