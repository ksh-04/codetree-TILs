prd = 1

a, b = map(int, input().split())

for i in range(a, b + 1):
    prd *= i

print(prd)