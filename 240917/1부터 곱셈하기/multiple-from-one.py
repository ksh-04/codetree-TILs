prd = 1

n = int(input())

for i in range(1, 11):
    prd *= i
    if prd >= n:
        print(i)
        break