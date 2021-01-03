n = int(input())

go = [[0] * 19 for _ in range(19)]

for i in range(n):
    x, y = map(int, input().split())
    for j in range(len(go)):
        for k in range(len(go[j])):
            go[x - 1][y - 1] = 1

for i in range(len(go)):
    for j in range(len(go[i])):
        print(go[i][j], end=' ')
    print()
