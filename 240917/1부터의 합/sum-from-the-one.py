sum = 0

n = int(input())

for i in range(1, 101):
    sum += i
    if sum >= n:
        print(i)
        break