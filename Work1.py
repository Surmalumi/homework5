#Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем

f = open('text.txt', 'w', encoding='utf-8')
while True:
    s = input(f'Введите текст: ')
    if s == '':
        break
    f.write(s+'\n')
f.close()