# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.

file = open('work2.txt', encoding='utf-8')
line = 0
for i in file:
    line += 1
    symbol = 0
    word = 0
    for a in i:
        if a != ' ' and symbol == 0:
            word += 1
            symbol = 1
        elif a == ' ':
            symbol = 0

    print(i, len(i), 'символов', word, 'слов(а, о)')

print(line, 'строки.')
file.close()