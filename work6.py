# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.

import re

dict = {}
with open('work6.txt','r', encoding='utf-8') as file:
    new_file = file.readlines()
    for discipline in new_file: 
        total_hours = 0
        hours = re.findall(r'\d+', discipline) 
        for hour in hours: 
            total_hours += float(hour) 
        dict[discipline.split()[0]] = total_hours 
    print(dict)

