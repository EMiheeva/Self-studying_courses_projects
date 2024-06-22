import pandas as pd
path_to_csv = 'StudentsPerformance.csv'
df = pd.read_csv(path_to_csv)
"""
Задача:
Как различается среднее и дисперсия оценок по предметам у групп студентов со стандартным или урезанным ланчем?
"""

standart_lunch_query = (df['lunch'] == 'standard')
free_red_lunch_query = (df['lunch'] == 'free/reduced')

lessons = list(df.columns)[-3:]
for lesson in lessons:
    print(f'lesson: {lesson}; standard: {df.loc[standart_lunch_query, lesson].mean()}; free: {df.loc[free_red_lunch_query, lesson].mean()}')

for lesson in lessons:
    print(f'lesson: {lesson}; standard: {df.loc[standart_lunch_query, lesson].var()}; free: {df.loc[free_red_lunch_query, lesson].var()}')