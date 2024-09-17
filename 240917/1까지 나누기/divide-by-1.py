i = 1
cnt = 0

n = int(input())

while n > 1:
    n = n // i
    i += 1
    cnt += 1
print(cnt)