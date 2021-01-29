# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.

def summary():
    try:
        with open('work5.txt', 'w+') as file:
            line = input(f'Введите набор чисел через пробел: \n')
            file.writelines(line)
            my_numb = line.split()

            print(sum(map(int, my_numb)))
    except ValueError:
        print('Error in number')
summary()

#f = open('work5.txt', 'a+') - не смогла допридумать как еще дописать в тот же файл результат сложения.(

