w, h, b = map(int, input().split())
space_bit = w * h * b
space_mb = space_bit / (8 * ((2 ** 10) ** 2))
print("%.2f MB" % space_mb)