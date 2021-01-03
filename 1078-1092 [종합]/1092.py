x, y, z = map(int, input().split())

day = 1

while((day % x != 0) or (day % y != 0) or (day % z != 0)):
    day +=1
print(day)