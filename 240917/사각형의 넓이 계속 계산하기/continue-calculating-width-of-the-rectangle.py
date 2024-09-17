while True:
    a = input().split()

    a[0] = int(a[0])
    a[1] = int(a[1])
    print(f"{a[0] * a[1]}")
    if a[2] == 'C':
        break