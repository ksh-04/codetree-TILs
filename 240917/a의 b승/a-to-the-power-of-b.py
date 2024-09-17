a, b = map(int, input().split())
prd = a
for _ in range(b-1):
    prd *= a

print(prd)