n = int(input())
answer = True

for i in range(2, n):
    if n % i == 0:
        answer = False
        break

if answer == True:
    print("N")
else:
    print("C")