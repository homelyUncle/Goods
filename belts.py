import json
import write_data, adding
import time

FILE_PATH = 'belts_data.json'

def write_all(path, data):
    with open(path, 'w', encoding='utf-8') as write_file:
        json.dump(data, write_file)

def read_all(path):
    with open(path, 'r', encoding='utf-8') as read_file:
        data = json.load(read_file)
        return data


def main(file_path):
    global all_data

    try:
        all_data = read_all(file_path)
    except FileNotFoundError:
        print('file does not exist')
        to_make_file = input('Do you want to create file and add some data? (y/n)\n')
        if to_make_file == 'y':
            all_data[0] = write_data.add_line()
            print(f'\n### item {all_data} added ###')
        else:
            print('thank you for using my app')
            time.sleep(2)
            raise SystemExit(0)


    while(True):
        ask = input("what do you want to do?"
                    "\n\t\t'i' to see one item"
                    "\n\t\t's' to see all items"
                    "\n\t\t'a' to add some items"
                    "\n\t\t'q' for quite program):\n")
        if ask == 's':
            print('\n')
            for i in all_data:
                print(i)
            print('\n')
        elif ask == 'a':
            all_data = all_data.append(adding.add(all_data))
        elif ask == 'f':
            pass
        elif ask == 'q':
            write_all(FILE_PATH, all_data)
            print('thank you for using my app')
            time.sleep(2)
            raise SystemExit(0)




    # write_all(file_path)

if __name__ == '__main__':
    main(FILE_PATH)
