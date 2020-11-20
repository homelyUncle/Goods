import os
import time
import json

FILE_PATH = 'belts_data.json'


def add():
    data = add_line()
    print(f"\n\t\t- - товар <{data['name']}> добавлен в список - -\n")
    return data


def add_line():

    # запрос названия до получения корректного значения...
    def input_type():
        name = input('Введите название: ')
        if name == '':  # ...исключая пустые строки...
            print("\t\tВы ничего не ввели")
            name = input_type()
        elif len(name) > 16:  # ...и исключая названия длиннее
            print('\t\tВведённое название слишком длинное (max 16)')
            name = input_type()
        return name

    # постоянный запрос количества до получения корректного значения...
    def input_nums():
        count = input('Введите количество: ')
        try:
            count = int(count)
        except ValueError:  # ...исключая возможность ввода литер
            print('\t\tВы ввели не число')
            count = input_nums()
        return count

    type_of_belt = input_type()
    count_of_belt = input_nums()

    res = {'name': type_of_belt, 'count': count_of_belt}
    # возвращем словарь (key: str, value: int)
    return res


def write_to_file(path, data):
    with open(path, 'w', encoding='utf-8') as write_file:
        json.dump(data, write_file, indent=4)


def read_from_file(path):
    with open(path, 'r', encoding='utf-8') as read_file:
        data = json.load(read_file)
        return data


def end():
    print('\n\t\t- - спасибо за использование программы - -\n')
    time.sleep(1)
    raise SystemExit(0)


def main(file_path):  # запуск программы
    all_data = []

    try:
        all_data = read_from_file(file_path)  # попытка чтения файла и записи данных в переменную
    except FileNotFoundError:  # создаём новый файл
        print('\n\t\t- - ФАЙЛ С ДАННЫМИ ОТСУТСВУЕТ - -\n')
        to_make_file = input('Хотите добавить запись? (y/n)\n')
        if to_make_file == 'y' or to_make_file == 'Y' or to_make_file == 'н' or to_make_file == 'Н':
            all_data = [add()]
        else:
            end()

    while True:
        action = input("Что нужно сделать?"  # типа меню
                       "\n\t\t's' показать все товары"
                       "\n\t\t'i' показать информацию об одном товаре"
                       "\n\t\t'z' показать товары, отсутствующие на складе"
                       "\n\t\t'a' добавить товар в список"
                       "\n\t\t'c' очистить экран"
                       "\n\t\t'q' выйти из программы\n")

        if action == 's' or action == 'S' or action == 'ы' or action == 'Ы':   # вывод всего списка
            for i in range(len(all_data)):
                j = all_data[i]
                if j['count'] == 0:
                    warn = '\t-- ТОВАРА НЕТ НА СКЛАДЕ!!! --'
                elif j['count'] < 2:
                    warn = '\t-- ПОСЛЕДНИЙ!!! --'
                elif j['count'] < 3:
                    warn = '\t-- ПОСЛЕДНИЕ!!! --'
                else:
                    warn = ''
                print(f"\t\t{i + 1} ->\t{j['name']} ____ {j['count']} {warn}")
            print()

        elif action == 'a' or action == 'A' or action == 'ф' or action == 'Ф':  # добавление записи
            all_data.append(add())

        elif action == 'i' or action == 'I' or action == 'ш' or action == 'Ш':  # вывод информации об одной записи
            choose = input('введите название/часть названия товара, который нужно найти: ')
            for i in all_data:
                if choose in i['name']:
                    out = f"\t{i['name']} ____ {i['count']}"
                    print(out)
            print()

        elif action == 'z' or action == 'Z' or action == 'я' or action == 'Я':  # вывод записей с нулевыми значениями
            print('\n\t-- ТОВАРА, ОТСУТСТВУЮЩИЙ НА СКЛАДЕ --')
            for i in all_data:
                if i['count'] == 0:
                    print(f"\t\t{i['name']}")
            print()

        elif action == 'q' or action == 'Q' or action == 'й' or action == 'Й':  # закрытие программы
            write_to_file(FILE_PATH, all_data)
            end()

        elif action == 'c' or action == 'C' or action == 'с' or action == 'С':  # очистка экрана
            os.system('cls')


if __name__ == '__main__':
    main(FILE_PATH)
