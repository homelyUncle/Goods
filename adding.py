import write_data


def add():
    data = write_data.add_line()
    print(f"\n\t\t- - item <{data['name']}> added - -\n")
    return data
