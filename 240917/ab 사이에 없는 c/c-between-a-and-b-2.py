answer = True

a, b, c = map(int, input().split())

for i in range(a, b+1):
    if i % c == 0:
        answer = False
        break
    
if answer == True:
    print("YES")
else:
    print("NO")