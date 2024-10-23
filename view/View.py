from controller.controller import Controller

# Основной рабочий скрипт для вывода меню задания и его исполнения.
# Все задания соответственно пронумерованы как в тз.

menu = """
1. Создать базу данных и таблицу
2. Добавить нового сотрудника
3. Показать всех сотрудников
4. Добавить 1000000 сотрудников.
5. Показать результат выборки из всех сотрудников с замером времени(не оптимизировано).
6. Показать результат выборки из всех сотрудников с замером времени(оптимизировано).
7. Удалить Таблицу.
0. Выйти из приложения"""


def view():
    controller = Controller()
    # create_db = False
    while True:
        print(f"{menu}\n")
        choice = input("Введите цифру: ")
        match choice:
            case "1":
                controller.create_table()
            case "2":
                if controller.table_is_created():
                    first_name = input("Введите Имя: ")
                    middle_name = input("Введите Фамилию: ")
                    last_name = input("Введите Отчество: ")
                    birthdate = input("Введите полную дату рождения: ")
                    sex = input("Введите Пол из двух -> (male/female): ")
                    if not sex or sex not in ("male", "female"):
                        sex = "male"
                    controller.insert_data(first_name, middle_name, last_name, birthdate, sex)
            case "3":
                controller.show_data()
            case "4":
                controller.execute_large_request()
            case "5":
                controller.show_all_employees_for_large_request()
            case "6":
                controller.show_all_employees_for_large_request_not_optimal()
            case "7":
                controller.drop_table()
            case "0":
                print("Выход из приложения")
                break
            case _:
                print("Неверный ввод.")
                continue
