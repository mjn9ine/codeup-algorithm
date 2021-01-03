h, b, c, s = map(int, input().split())
space_bit = h * b * c * s
space_mb = space_bit / (8 * ((2 ** 10) ** 2))
print(round(space_mb, 1), "MB")