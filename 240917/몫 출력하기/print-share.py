cnt = 0

while True:
    n = int(input())

    if n % 2 != 0:
        continue
    else:
        cnt += 1
        print(f"{n // 2}")
        if cnt == 3:
            break