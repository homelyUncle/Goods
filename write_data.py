def add_line():

    # постоянный запрос названия до получения корректного значения...
    while True:
        type_of_belt = input('Input type of belts: ')
        if type_of_belt == '':  # ...исключая пустые строки...
            print("\t\tYou didn't write anything")
            continue
        elif len(type_of_belt) <= 16 and type_of_belt != '':
            break
        else:  # ...и исключая названия длиннее
            print('\t\tThe name you entered is too long')

    # постоянный запрос количества до получения корректного значения...
    while True:
        count_of_belt = input('Input count of belts: ')
        try:
            int(count_of_belt)
            break
        except ValueError:  # ...исключая возможность ввода литер
            print('\t\tYou entered not an integer')

    # регулирование количества "табуляций" для выравнивания таблицы
    tab = '\t'
    if len(type_of_belt) < 4:
        tab *= 5
    elif len(type_of_belt) < 8:
        tab *= 4
    elif len(type_of_belt) < 12:
        tab *= 3
    elif len(type_of_belt) < 16:
        tab *= 2

    # возвращем данные (key, value)
    return type_of_belt, count_of_belt
