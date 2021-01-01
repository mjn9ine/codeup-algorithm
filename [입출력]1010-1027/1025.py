num = input()

for i in range(len(num)):
    print("[{}]".format(int(num[i])*(10**(len(num)-i-1))))