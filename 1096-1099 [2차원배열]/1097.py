go = [[0] * 19 for _ in range(19)]

for i in range(19):
    l = input().split()
    for j in range(19):
        go[i][j] = int(l[j])

n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    for j in range(19):
        if(go[x - 1][j] == 0):
            go[x - 1][j] = 1
        else:
            go[x - 1][j] = 0
    for j in range(19):
        if(go[j][y - 1] == 0):
            go[j][y - 1] = 1
        else:
            go[j][y - 1] = 0
for i in range(19):
    for j in range(19):
        print(go[i][j], end=' ')
    print()
