# оздать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.

with open('work3.txt', 'r', encoding='utf-8') as my_file:
    salary = []
    name = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
           name.append(i[0])
        salary.append(i[1])
print(f'Сотрудники с окладом меньше 20.000 {name}, средний оклад в фирме {sum(map(int, salary)) / len(salary)}')