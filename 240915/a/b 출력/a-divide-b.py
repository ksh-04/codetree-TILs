a, b = map(int, input().split())

print(int(a/b), ".", sep = "", end = "")
a = a * 10
for _ in range(20):
    print(int(a/b), end = "")
    a = a - b * int(a/b)