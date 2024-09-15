a, b = map(int, input().split())

print(int(a/b), ".", sep = "", end = "")
for _ in range(20):
    a = a * 10
    print(int(a/b), end = "")
    a = a - b * int(a/b)