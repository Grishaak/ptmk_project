from controller.controller import Controller

menu = """
1. Создать базу данных и таблицу
2. Добавить нового сотрудника
3. Показать всех сотрудников
4. Добавить 1000000 сотрудников.
5. Показать результат выборки из всех сотрудников с замером времени.
0. Выйти из приложения"""


def view():
    controller = Controller()
    # create_db = False
    while True:
        print(f"{menu}\n")
        choice = int(input("Введите цифру: "))
        match choice:
            case 1:
                controller.create_database()
                controller.create_table()
            case 2:
                first_name = input("Введите Имя: ")
                middle_name = input("Введите Фамилию: ")
                last_name = input("Введите Отчество: ")
                birthdate = input("Введите полную дату рождения: ")
                sex = input("Введите Пол из двух -> (male/female): ")
                if not sex or sex not in ("male", "female"):
                    sex = "male"
                controller.insert_data(first_name, middle_name, last_name, birthdate, sex)
            case 3:
                controller.show_data()
            case 4:
                pass
            case 5:
                pass
            case 0:
                print("Выход из приложения")
                controller.close_connection()
                break
