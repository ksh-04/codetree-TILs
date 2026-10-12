n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

A = [0 for _ in range(2000)]
idx = 1000
for xi, di in zip(x, dir):
    if di == 'L':
        for _ in range(xi):
            idx -= 1
            A[idx] += 1
    else:
        for _ in range(xi):
            A[idx] += 1
            idx += 1

answer = 0
for a in A:
    if a > 1:
        answer += 1
print(answer)