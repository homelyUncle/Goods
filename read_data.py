import os


def file_exists(file_path):
    exists = os.path.exists(file_path)
    return exists


# выводит содержание всего файла
def read_file(file_path):
    if file_exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            data = file.read()
            return data
    else:
        return f'file {file_path} does not exist'


# ищет и выводит количество запрошенных ремней
def read_line(file_path, content: str):
    if file_exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            data = file.readlines()
            for line in data:
                line_list = line.rstrip().split('\t')
                print(line_list[0])
                if content == line_list[0]:
                    count_of_item = int(line_list[-1])
                    return f'is now available {count_of_item} pcs of {content}'
                else:
                    continue
            return f'there is no {content} in this list'
    else:
        return f'file {file_path} does not exist'
