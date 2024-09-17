while True:
    n = int(input())
    if n == 25:
        print("Good")
        break
    elif n < 25:
        print("Higher")
        continue
    else:
        print("Lower")
        continue