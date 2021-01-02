integers = list(map(int, input().split()))

for i, num in enumerate(integers):
    if (num != 0):
        print(num)
    else:
        break