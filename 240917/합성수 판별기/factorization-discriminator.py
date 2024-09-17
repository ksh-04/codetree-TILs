n = int(input())
answer = True

for i in range(1, n):
    if n % i == 0:
        answer = False
        break

if answer == True:
    print("N")
else:
    print("C")