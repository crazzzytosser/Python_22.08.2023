import csv
import datetime


def create_note():
    note_id = input("Введите идентификатор заметки: ")
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    created = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    modified = created

    with open('notes.csv', 'a', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow([note_id, title, body, created, modified])

    print("Заметка создана успешно.")


def open_note():
    note_id = input("Введите идентификатор заметки: ")

    with open('notes.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            if row[0] == note_id:
                print("Идентификатор: ", row[0])
                print("Заголовок: ", row[1])
                print("Текст: ", row[2])
                print("Дата создания: ", row[3])
                print("Дата последнего изменения: ", row[4])
                return

    print("Заметка с указанным идентификатором не найдена.")


def edit_note():
    note_id = input("Введите идентификатор заметки: ")

    with open('notes.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        notes = list(reader)

    found = False
    with open('notes.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for row in notes:
            if row[0] == note_id:
                modified = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                row[4] = modified
                writer.writerow(row)
                found = True
            else:
                writer.writerow(row)

    if found:
        print("Заметка успешно отредактирована.")
    else:
        print("Заметка с указанным идентификатором не найдена.")


def delete_note():
    note_id = input("Введите идентификатор заметки: ")

    with open('notes.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        notes = list(reader)

    found = False
    with open('notes.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for row in notes:
            if row[0] == note_id:
                found = True
            else:
                writer.writerow(row)

    if found:
        print("Заметка успешно удалена.")
    else:
        print("Заметка с указанным идентификатором не найдена.")


def display_notes():
    with open('notes.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            print()
            print("Идентификатор: ", row[0])
            print("Заголовок: ", row[1])
            print()


def main_menu():
    while True:
        print("\nМеню:")
        print("1. Создать заметку")
        print("2. Открыть заметку")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Вывести на экран все заметки")
        print("6. Закрыть программу")

        choice = input("Выберите пункт меню: ")

        if choice == "1":
            create_note()
        elif choice == "2":
            open_note()
        elif choice == "3":
            edit_note()
        elif choice == "4":
            delete_note()
        elif choice == "5":
            display_notes()
        elif choice == "6":
            print("Программа завершена.")
            break
        else:
            print("Неверный выбор. Пожалуйста, повторите.")


if __name__ == "__main__":
    main_menu()