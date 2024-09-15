a, b = map(int, input().split())

print(a // b, ".", sep = "", end = "")
for _ in range(20):
    a = a * 10
    print(a // b, end = "")
    a = a - b * (a // b)