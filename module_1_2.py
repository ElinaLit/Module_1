name = 'Курс: Python'
name_lesson = ' всего задач'
lesson = 12
name_time = ' затрачено часов'
time = 1.5
name_time_average = ' среднее время выполнения'
time_average = time/lesson
comma =','
colon = ':'
print(name,comma, name_lesson,colon, lesson, comma, name_time,colon, time, comma, name_time_average, colon, time_average, '.',sep ="")
print(f'Курс: Pyton, всего задач: {lesson}, затрачено часов {time}, среднее время выполнения: {time_average}')