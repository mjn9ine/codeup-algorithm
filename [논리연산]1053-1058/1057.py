x, y = map(int, input().split())
x, y = bool(x), bool(y)
print(int(not(x ^ y)))