#
# Необходимо написать программу, которая составляет словарь,
# используя grades и students, где ключом будет имя ученика, а значением - его средний балл
#

grades = ['5 3 3 5 4', '2 2 2 3', '4 5 5 2', '4 4 3', '5 5 5 4 5']
students = {'Johnni', 'Bilbo', 'Steve', 'Kendrick', 'Aaron'}
average_score = {}
students = sorted(list(students))
middle = 0
for i in range(len(students)):
    grades[i] = grades[i].split(' ')
    sum = 0
    for j in range(len(grades[i])):
        sum += int(grades[i][j])
        middle = sum / len(grades[i])
    average_score[students[i]] = middle
print(average_score)
