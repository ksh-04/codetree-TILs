answer = True

for _ in range(5):
    n = int(input())
    if n % 3 != 0:
        answer = False

if answer == True:
    print(1)
else:
    print(0)