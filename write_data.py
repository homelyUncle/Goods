def add_line():

    # запрос названия до получения корректного значения...
    def input_type():
        name = input('Input type of belts: ')
        if name == '':  # ...исключая пустые строки...
            print("\t\tYou didn't write anything")
            input_type()
        elif len(name) > 16:  # ...и исключая названия длиннее
            print('\t\tThe name you entered is too long')
            input_type()
        return name

    # постоянный запрос количества до получения корректного значения...
    def input_nums():
        count_int = 0
        count = input('Input count of belts: ')
        try:
            count_int = int(count)
        except ValueError:  # ...исключая возможность ввода литер
            print('\t\tYou entered not an integer')
            input_nums()
        return count_int

    type_of_belt = input_type()
    count_of_belt = input_nums()
    ret = {type_of_belt: count_of_belt}
    # возвращем данные (key: str, value: int)
    return ret
