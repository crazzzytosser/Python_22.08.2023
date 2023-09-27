import os

FILE_NAME = 'phone.txt'


def main():
    data = {}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME) as f:
            for line in f.readlines():
                if line:
                    name, num = line.split("\t")
                    data[name] = num
    else:
        with open(FILE_NAME, "w") as f:
            pass

    while True:
        while True:

            print("1. Ввести данные: ")
            print("2. Поиск: ")
            print("3. Изменить или удалить данные: ")
            print("4. Выход: ")
            user_choice = input("Input: ")
            if user_choice not in ['1', '2', '3', '4']:
                print("err")
            else:
                break
        match user_choice:
            case "1":
                data = input_data(data)
            case "2":
                search_data(data)
            case "3":
                update_or_delete(data)
            case "4":
                print("Exit")
                if not data:
                    return
                with open(FILE_NAME, "w") as f:
                    for name in data:
                        print(f"{name}\t{data[name]}", file=f)
                return


def input_data(data):
    name = input("Input name: ")
    if name and len(name.split(' ')) == 3:
        num = input("Введите номер телефона: ")
        if num and num.isdigit():
            data[name.replace('\t', " ")] = num
            return data
    print("Неверный ввод данных: ")
    return data


def search_data(data):
    user_input = input("Введите данные для поиска: ")
    while True:
        print("1. Найти фамилию: ")
        print("2. Найти имя: ")
        print("3. Найти отчество: ")
        print("4. Найти номер телефон: ")
        print("5. Назад в меню: ")
        user_choice = input("Input: ")
        if user_choice not in ['1', '2', '3', '4', '5']:
            print("err")
        else:
            break
    match user_choice:
        case "1":
            for key in data:
                name_1, name_2, name_3 = key.split()
                if name_1 == user_input:
                    print(f"{key} {data[key]}")
        case "2":
            for key in data:
                name_1, name_2, name_3 = key.split()
                if name_2 == user_input:
                    print(f"{key} {data[key]}")
        case "3":
            for key in data:
                name_1, name_2, name_3 = key.split()
                if name_3 == user_input:
                    print(f"{key} {data[key]}")
        case "4":
            for key, value in data.items():
                if value == user_input:
                    print(f"{key} {data[key]}")
        case "5":
            print("exit")
            return

def update_or_delete(data):
    while True:
        print("1. Изменить данные: ")
        print("2. Удалить данные: ")
        print("3. Выход: ")
        user_choice = input("Input: ")
        if user_choice not in ['1', '2', '3']:
            print("err")
        else:
            break

    if user_choice == '1':
        update(data)
    elif user_choice == '2':
        delete(data)
    elif user_choice == '3':
        print("Выход")

def update(data):
    input_data = input("Введите ФИО для изменения данных: ")
    if input_data in data:
        new_info = input("Введите новый номер телефона: ")
        if new_info.isdigit():
            data[input_data] = new_info
            print(" Сохранено!")
        else:
            print("Error!")

def delete(data):
    input_data = input("Введите ФИО для удаления данных: ")
    if input_data in data:
        del data[input_data]
        print("Данные удалены!")
    else:
        print("Error")


if __name__ == "__main__":
    main()
