sum = 0
cnt = 0

a, b = map(int, input().split())

for i in range(a, b+1):
    if i % 5 == 0 or i % 7 == 0:
        sum += i
        cnt += 1

avg = sum / cnt

print(f"{sum} {avg:.1f}")