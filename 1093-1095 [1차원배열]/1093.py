n = int(input())
x = list(map(int, input().split()))

student_list = [0] * 23

for i in x:
    student_list[i - 1] += 1

for student in student_list:
    print(student, end=' ')