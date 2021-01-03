char = input()
hexa_num = int(char, 16)
for i in range(1, 16):
    print(f"{char}*{format(i, 'X')}={format(hexa_num * i, 'X')}")