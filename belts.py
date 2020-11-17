import read_data as rd
import write_data as wd
import gui

FILE_PATH = 'belts.txt'

belts = {}

line = wd.add_line()
belts[line[0]] = line[1]

gui.

# сохранение фала перед закрытием приложения

# создание строки таблицы
new_string = f'{type_of_belt}{tab}|\t{count_of_belt}\n' \
                 f'————————————————————————————\n'
with open(FILE_PATH, 'a', encoding='utf-8') as file:
    file.write(new_string)

print(belts)
