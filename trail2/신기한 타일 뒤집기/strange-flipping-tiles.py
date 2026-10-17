n = int(input())

tiles = [0] * 200001
idx = 100000

for _ in range(n):
    x, d = input().split()
    x = int(x)

    if d == 'L':
        for i in range(idx, idx - x, -1):
            tiles[i] = 1
        idx -= x - 1

    else:
        for i in range(idx, idx + x):
            tiles[i] = 2
        idx += x - 1

print(tiles.count(1), tiles.count(2))