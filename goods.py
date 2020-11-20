import os
import time
import json

FILE_PATH = 'belts_data.json'


def edit():
    pass


def add():
    data = add_line()
    print(f"\n\t\t- - товар <{data['name']}> добавлен в список - -\n")
    return data


def add_line():
    # запрос названия до получения корректного значения...
    def input_type():
        name = input('Введите название: ')
        if name == '':  # ...исключая пустые строки...
            print("\tВы ничего не ввели")
            name = input_type()
        elif len(name) > 16:  # ...и исключая названия длиннее
            print('\tВведённое название слишком длинное (max 16)')
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
        print('\n\t- - ФАЙЛ С ДАННЫМИ ОТСУТСВУЕТ - -\n')
        to_make_file = input('Хотите добавить запись? (y/n)\n')
        if to_make_file == 'y' or to_make_file == 'Y' or to_make_file == 'н' or to_make_file == 'Н':
            all_data = [add()]
        else:
            end()

    while True:
        action = input("-= Главное меню =-"  # типа меню
                       "\n\t\t's' показать все товары"
                       "\t\t'i' показать один товар"
                       "\n\t\t'z' показать отсутствующее"
                       "\t'a' добавить товар в список"
                       "\n\t\t'c' очистить экран"
                       "\t\t'q' выйти из программы\n")

        if action == 's' or action == 'S' or action == 'ы' or action == 'Ы':  # вывод всего списка
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
                print(f"\t\t{i + 1}\t{j['name']} ____ {j['count']} {warn}")
            print()

        elif action == 'a' or action == 'A' or action == 'ф' or action == 'Ф':  # добавление записи
            all_data.append(add())

        elif action == 'i' or action == 'I' or action == 'ш' or action == 'Ш':  # вывод информации об одной записи
            founded = []
            ct = 0
            find_to_item = input('введите название/часть названия товара, который нужно найти: ')
            for i in all_data:
                if find_to_item in i['name']:
                    dic = {'name': i['name'], 'count': i['count']}
                    if len(founded) == 0:
                        founded = [dic]
                    else:
                        founded.append(dic)
                    out = f"\t{ct + 1}<\t{i['name']}\t>{i['count']}"
                    print(out)
                ct += 1
            if ct > 0:
                while True:
                    while True:
                        line = input('введите номер необходимой строки:')
                        try:
                            line = int(line)
                            break
                        except ValueError:  # ...исключая возможность ввода литер
                            print('\t\tВы ввели не число\n')
                    if line in range(ct):
                        break
                    else:
                        print('введён неверный номер')
                ct = line
                TODO: 'вынести в разные методы обработчикисобытий'

            choose_action = input("выберите действие:"
                                  "\n\t\t'с' изменить количество"
                                  "\t\t'n' изменить название"
                                  "\n\t\t'd' удалить запись"
                                  "\t\t\t'm' вернуться в 'главное меню'\n")
            if choose_action == 'c' or choose_action == 'C' or choose_action == 'с' or choose_action == 'С':
                change_count = input('Введите новое количество: ')
                print(change_count)

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
