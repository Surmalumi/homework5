# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4

num = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []

with open('work4.txt', 'r', encoding='utf-8') as file:
    for i in file:
        i = i.split(' ', 1)
        new_file.append(num[i[0]] + ' ' + i[1])
    print(new_file)


with open('text4.txt', 'w', encoding='utf-8') as new_f:
    new_f.writelines(new_file)
new_f.close()
