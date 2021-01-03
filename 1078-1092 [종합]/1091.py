a, m, d, n = map(int, input().split())

while(n - 1 > 0):
    n -= 1
    a = (a * m) + d

print(a)