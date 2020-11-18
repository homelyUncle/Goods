def add_line():

    # запрос названия до получения корректного значения...
    def input_type():
        name = input('Input type of belts: ')
        if name == '':  # ...исключая пустые строки...
            print("\t\tYou didn't write anything")
            name = input_type()
        elif len(name) > 16:  # ...и исключая названия длиннее
            print('\t\tThe name you entered is too long')
            name = input_type()
        return name

    # постоянный запрос количества до получения корректного значения...
    def input_nums():
        count = input('Input count of belts: ')
        try:
            count = int(count)
        except ValueError:  # ...исключая возможность ввода литер
            print('\t\tYou entered not an integer')
            count = input_nums()
        return count

    type_of_belt = input_type()
    count_of_belt = input_nums()

    res = {'name': type_of_belt, 'count': count_of_belt}
    # возвращем словарь (key: str, value: int)
    return res
