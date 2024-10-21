from contorl.Controller import Controller


def view():
    controller = Controller()
    create_db = False
    while True:
        choice = input("Введите цифру: ")
        match choice:
            case 1:
                controller.create_database()
                controller.create_table()
            case 2:
                first_name = input("Введите Имя: ")
                middle_name = input("Введите Фамилию: ")
                last_name = input("Введите Отчество: ")
                birthdate = input("Введите полную дату рождения: ")
                sex = input("Введите Пол (male/female): ")
                if not sex:
                    sex = "male"
                controller.insert_data(first_name, middle_name, last_name, birthdate, sex)
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 0:
                print("Выход из приложения")
                break
