sum, cnt = 0, 0
while True:
    age = int(input())
    if age < 20 or age > 29:
        break
    sum += age
    cnt += 1

avg = sum / cnt
print(f"{avg:.2f}")