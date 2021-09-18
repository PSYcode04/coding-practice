student = [1] * 30

for i in range(28):
    student[int(input())-1] = 0

for i in range(30):
    if student[i] == 1:
        print(i+1)