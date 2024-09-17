sum = 0
cnt = 0

n = int(input())

for _ in range(n):
    i = int(input())
    sum += i
    cnt += 1

avg = sum / cnt
print(f"{sum} {avg:.1f}")