from os import path
<<<<<<< HEAD
=======
import datetime

>>>>>>> f4a889a (created: read_records, show_all, add_new_entry, del_entry, change_entry, search_entry, existing_entry, mein_menu.)

file_base = "base.csv"
all_data = []
last_id = 0
<<<<<<< HEAD
=======
datetime = datetime.datetime.today()
dt = datetime.strftime("%d.%m.%Y %H:%M")

>>>>>>> f4a889a (created: read_records, show_all, add_new_entry, del_entry, change_entry, search_entry, existing_entry, mein_menu.)

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as  _:
        pass

def read_records():
    global all_data, last_id

    with open(file_base, "r", encoding="utf-8") as f:
        all_data = [i.strip() for i in f]
        if all_data:
            last_id = int(all_data[-1].split()[0])
        return all_data

def show_all():
    if not all_data:
        print("Данных нет!")
    else:
        print(*all_data, sep="\n")

def add_new_entry():
    global last_id
<<<<<<< HEAD

    array = ['header', 'information', 'date_time']
=======
    global dt

    array = ['Заголовок', 'Заметка']
>>>>>>> f4a889a (created: read_records, show_all, add_new_entry, del_entry, change_entry, search_entry, existing_entry, mein_menu.)
    answers = []
    for i in array:
        answers.append(data_collection(i))
    if not existing_entry(0, " ".join(answers)):
        last_id += 1
        answers.insert(0, str(last_id))

        with open(file_base, "a", encoding="utf-8") as f:
            f.write(f'{" ".join(answers)}\n')
        print("Запись успешно добавлена!\n")
    else:
        print("Запись уже существует!")

def del_entry():
    global all_data

    symbol = "\n"
    show_all()
    del_record = input("Введите ID: ")

    if existing_entry(del_record, ""):
        all_data = [k for k in all_data if k.split()[0] != del_record]

        with open(file_base, "w", encoding="utf-8") as f:
            f.write(f'{symbol.join(all_data)}\n')
        print("Запись удалена!")
    else:
        print("Данные неверны!")

def change_entry(data_tuple):
    global all_data

    symbol = "\n"
    record_id, num_data, data = data_tuple

    for i, v in enumerate(all_data):
        if v.split()[0] == record_id:
            v = v.split()
            v[int(num_data)] = data
            if existing_entry(0, " ".join(v[1:])):
                print("Запись уже существует!")
                return
            all_data[i] = " ".join(v)
            break

    with open(file_base, "w", encoding="utf-8") as f:
        f.write(f'{symbol.join(all_data)}\n')
    print("Запись изменена!\n")

def search_entry():

    search_data = existing_entry(0, input("Введите данные для поиска: "))
    if search_data:
        print(*search_data, sep="\n")
    else:
        print("Данные неверны!")

def existing_entry(rec_id, data):

    if rec_id:
<<<<<<< HEAD
        candidates = [i for i in all_data if rec_id in i.split([0])]
=======
        candidates = [i for i in all_data if rec_id in i.split()[0]]
>>>>>>> f4a889a (created: read_records, show_all, add_new_entry, del_entry, change_entry, search_entry, existing_entry, mein_menu.)
    else:
        candidates = [i for i in data if data in i]
    return candidates

def data_collection(num):

    answer = input(f"Введите {num}: ")
<<<<<<< HEAD
    while True:
        if num in "header information":
            if len(answer) == 1:
                break
        answer = input(f"Данные неверны!\n"
                       f"В записи должно быть не меньше одного символа!\n"
=======
    str = ""
    while True:
        if num in "Заголовок Заметка":
            if not str:
                break
        answer = input(f"Данные неверны!\n"
                       f"В записи должно быть не менее одного символа!\n"
>>>>>>> f4a889a (created: read_records, show_all, add_new_entry, del_entry, change_entry, search_entry, existing_entry, mein_menu.)
                       f"Введите {num}: ")
    return answer

def main_menu():

    play = True
    while play:
        read_records()
<<<<<<< HEAD
        answer = input("Заметки:\n"
                       "1. Покакзать все записи\n"
=======
        answer = input("Меню: \n"
                       "1. Покакать все записи\n"
>>>>>>> f4a889a (created: read_records, show_all, add_new_entry, del_entry, change_entry, search_entry, existing_entry, mein_menu.)
                       "2. Добавить запись\n"
                       "3. Поиск записи\n"
                       "4. Изменить запись\n"
                       "5. Удалить запись\n"
<<<<<<< HEAD
                       "6. Импорт/экспорт\n"
                       "7. Выход\n")
=======
                       "6. Выход\n")
>>>>>>> f4a889a (created: read_records, show_all, add_new_entry, del_entry, change_entry, search_entry, existing_entry, mein_menu.)
        match answer:
            case "1":
                show_all()
            case "2":
                add_new_entry()
            case "3":
                search_entry()
            case "4":
                work = edit_menu()
                if work:
                    change_entry(work)
            case "5":
                del_entry()
            case "6":
<<<<<<< HEAD
                exp_imp_menu()
            case "7":
=======
>>>>>>> f4a889a (created: read_records, show_all, add_new_entry, del_entry, change_entry, search_entry, existing_entry, mein_menu.)
                play = False
            case _:
                print("Попробуйте ещё раз!\n")

<<<<<<< HEAD
=======
def edit_menu():

    add_dict = {"1": "Заголовок", "2": "Заметка"}
    show_all()
    record_id = input("Введите ID: ")

    if existing_entry(record_id, ""):
        while True:
            print("\nИзменить:")
            change = input("1. Заголовок\n"
                           "2. Заметка\n"
                           "3. Выход\n")
            match change:
                case "1" | "2":
                    return record_id, change, data_collection(add_dict[change])
                case "3":
                    return 0
                case _:
                    print("Данные введены не верно.")
    else:
        print("Данные не верны!")

main_menu()
>>>>>>> f4a889a (created: read_records, show_all, add_new_entry, del_entry, change_entry, search_entry, existing_entry, mein_menu.)
