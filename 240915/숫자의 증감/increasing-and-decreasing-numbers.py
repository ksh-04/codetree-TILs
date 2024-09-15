a = input().split()

if a[0] == 'A':
    for i in range(1, int(a[1])+1):
        print(i, end = " ")
elif a[0] == 'D':
    for i in range(int(a[1]), 0, -1):
        print(i, end = " ")