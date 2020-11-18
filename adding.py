import write_data

def add(all_data):
    data = write_data.add_line()
    all_data = all_data.append(data)
    print(f'\n### belt {data} added ###\n')
    return all_data