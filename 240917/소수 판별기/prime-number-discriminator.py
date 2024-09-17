answer = True
n = int(input())

for i in range(2, n):
    if n % i == 0:
        answer = False
        break

if answer == False:
    print("C")
else:
    print("P")