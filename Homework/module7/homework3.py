team1_num = 5
score_1 = 40
team1_time = 18015.5

team2_num = 6
score_2 = 42
team2_time = 20000

challenge_result = None
tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time) / tasks_total
# Форматирование строк с использованием %
print('В команде «Мастера кода» участников: %d!' % team1_num)
print('Итого сегодня в командах участников: %d и %d!' % (team1_num, team2_num))

# Форматирование строк с использованием format()
print('Команда «Волшебники данных» решила задач: {}!'.format(score_2))
print('Команда «Волшебники данных» решили задачи за: {} c!'.format(team2_time))

# Форматирование строк с использованием f-строки
print(f'Команды решили {score_1} и {score_2} задач.')
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Мастера кода'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Волшебники Данных'
else:
    challenge_result = 'Ничья'

if challenge_result != 'Ничья':
    print(f'Победа команды «{challenge_result}»!')

print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')
