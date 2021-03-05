import os
import time
import json
from sys import platform

FILE_PATH = 'belts_data.json'


def input_nums():
    count = input('Введите количество: ')
    try:
        count = int(count)
    except ValueError:  # ...исключая возможность ввода литер
        print('\t\tВы ввели не число')
        count = input_nums()
    return count


def input_type():
    name = input('Введите название: ')
    if name == '':  # ...исключая пустые строки...
        print("\tВы ничего не ввели")
        name = input_type()
    elif len(name) > 16:  # ...и исключая названия длиннее
        print('\tВведённое название слишком длинное (max 16)')
        name = input_type()
    return name


def find(all_items, item_to_find):
    separator = '\t|\t'
    founded_index = []
    ct = 0
    for i in all_items:
        if item_to_find in i['name'].lower():
            if len(founded_index) == 0:
                founded_index = [all_items.index(i)]
            else:
                founded_index.append(all_items.index(i))
            print(f"\t{ct + 1}\t{i['name']:15}\t{i['count']:3}", end=f'{separator:6}')
            if ct % 2 == 1:
                print()
        else:
            continue
        ct += 1
    print()
    if ct > 1:
        while True:
            while True:
                line = input('введите номер необходимой строки: ')
                try:
                    line = int(line)
                    break
                except ValueError:  # ...исключая возможность ввода литер
                    print('\t\tВы ввели не число\n')
            if line - 1 in range(ct):
                break
            else:
                print('введён неверный номер')
        return founded_index[line - 1]
    else:
        return founded_index[ct - 1]


def show_all(all_items):
    separator = '\t|\t'
    print('-= ОБЩИЙ СПИСОК =-')
    for i in range(len(all_items)):
        j = all_items[i]
        if j['count'] < 3:
            warn = '*'
        else:
            warn = ''
        print(f"\t{(i + 1)}\t{j['name']:15} ===> {j['count']:3} {warn}", end=f'{separator:6}')
        if i % 2 == 1:
            print()
    print('* - мало на складе')


def add():
    data = add_line()
    print(f"\n\t\t- - <{data['name']}> добавлен в список - -\n")
    return data


def add_line():
    # запрос названия до получения корректного значения...
    type_of_belt = input_type()
    # постоянный запрос количества до получения корректного значения...
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


def clear_screen():
    if platform == "win32":
        command = 'cls'
    else:
        command = 'clear'
    os.system(command)


def end():
    print('\n\t\t- - спасибо за использование программы - -\n')
    time.sleep(1)
    raise SystemExit(0)


def main(file_path):  # запуск программы
    main_list = []

    try:
        main_list = read_from_file(file_path)  # попытка чтения файла и записи данных в переменную
    except FileNotFoundError:  # создаём новый файл
        print('\t- - ФАЙЛ С ДАННЫМИ ОТСУТСВУЕТ - -\n')
        to_make_file = input('Хотите добавить запись? (y/n)\n')
        if to_make_file in ('y', 'Y', 'н', 'Н'):
            main_list = [add()]
            write_to_file(FILE_PATH, main_list)
        else:
            end()

    while True:
        print()
        main_menu = input("-= ГЛАВНОЕ МЕНЮ =-"  # типа меню
                          "\n\t[s] показать всё\t[i] редактировать"
                          "\n\t[z] закончились\t\t[a] добавить в список"
                          "\n\t[c] очистить экран\t[q] выйти из программы\n")

        if main_menu in ('s', 'S', 'ы', 'Ы'):  # вывод всего списка
            clear_screen()
            show_all(main_list)

        elif main_menu in ('a', 'A', 'ф', 'Ф'):  # добавление записи
            clear_screen()
            main_list.append(add())
            write_to_file(FILE_PATH, main_list)

        elif main_menu in ('i', 'I', 'ш', 'Ш'):
            clear_screen()
            print('-= ПОИСК =-')
            # вывод информации об одной записи
            finding_item = input('введите название/часть названия того, что нужно отредактировать:')
            try:
                index_changing_count = main_list[find(main_list, finding_item.lower())]
            except IndexError:
                print('\nЗАПИСЬ НЕ НАЙДЕНА')
                continue
            clear_screen()
            print(f"выбран: {index_changing_count['name']}\n")
            choose_action = input("выберите действие:"
                                  "\n\t'с' изменить количество\t\t'n' изменить название"
                                  "\n\t'd' удалить запись\t\t'm' вернуться в 'главное меню'\n")
            if choose_action in ('c', 'C', 'с', 'С'):
                index_changing_count['count'] = input_nums()
                print(f"\n\t{index_changing_count['name']} ____ {index_changing_count['count']}\n")
                write_to_file(FILE_PATH, main_list)

            if choose_action in ('n', 'N', 'т', 'Т'):
                index_changing_count['name'] = input_type()
                print(f"\n\t{index_changing_count['name']} ____ {index_changing_count['count']}\n")
                write_to_file(FILE_PATH, main_list)

            if choose_action in ('d', 'D', 'в', 'В'):
                main_list.remove(index_changing_count)
                write_to_file(FILE_PATH, main_list)

            if choose_action in ('m', 'M', 'ь', 'Ь'):
                clear_screen()
                continue

        elif main_menu in ('z', 'Z', 'я', 'Я'):
            clear_screen()
            # вывод записей с нулевыми значениями
            print('\t-= ТОВАР, ОТСУТСТВУЮЩИЙ НА СКЛАДЕ =-')
            for i in main_list:
                if i['count'] == 0:
                    print(f"\t\t{i['name']}")

        elif main_menu in ('q', 'Q', 'й', 'Й'):  # закрытие программы
            write_to_file(FILE_PATH, main_list)
            end()

        elif main_menu in ('c', 'C', 'с', 'С'):  # очистка экрана
            clear_screen()


if __name__ == '__main__':
    main(FILE_PATH)
