arr = list(map(int, input().split()))
sum, avg, count = 0, 0, 0
for i in range(len(arr)):
    if arr[i] >= 250:
        break
    else:
        sum += arr[i]
        count += 1

avg = sum / count
print(f"{sum} {avg:.1f}")