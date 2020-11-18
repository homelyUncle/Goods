import time
import adding
import json_


def main(file_path):  # запуск программы

    try:
        all_data = json_.read_from_file(file_path)  # попытка чтения файла и записи данных в переменную
    except FileNotFoundError:  # создаём новый файл
        print('\n\t\t- - file does not exist - -\n')
        to_make_file = input('Do you want to create the file and add some data? (y/n)\n')
        if to_make_file == 'y':
            all_data = [adding.add()]
        else:
            print('\n\t\t- - thank you for using my app - -\n')
            time.sleep(1)
            raise SystemExit(0)

    while True:
        action = input("what do you want to do?"  # типа меню
                       "\n\t\t'i' to see info about one item"
                       "\n\t\t's' to see all items"
                       "\n\t\t'a' to add some items"
                       "\n\t\t'r' for modify info"
                       "\n\t\t'q' for quite program:\n")

        if action == 's':  # вывод всего списка
            for i in range(len(all_data)):
                j = all_data[i]
                print(f"\t\t{i + 1} ->\t{j['name']}\t {j['count']}")
            print()
        elif action == 'a':  # добавление записи
            all_data.append(adding.add())
        elif action == 'i':  # вывод информации об одной записи
            pass
        elif action == 'r':  # редактирование записи
            pass
        elif action == 'q':  # закрытие программы
            json_.write_to_file(json_.FILE_PATH, all_data)
            print('thank you for using app')
            time.sleep(2)
            raise SystemExit(0)


if __name__ == '__main__':
    main(json_.FILE_PATH)
