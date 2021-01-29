# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.

import re

dict = {}
with open('work6.txt','r', encoding='utf-8') as file:
    new_file = file.readlines()
    for discipline in new_file: #пробегаем по списку из строк, полученному из readlines
        total_hours = 0
        hours = re.findall(r'\d+', discipline) #ищем в строке числа и формируем из них список
        for hour in hours: #пробегаем по сформированному списку из чисел
            total_hours += float(hour) #добавляем float от числа к сумме
        dict[discipline.split()[0]] = total_hours #первое слово в строке - название предмета, его добавляем как key, а сумму - как value
    print(dict)

