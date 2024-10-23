from model.Manager import Manager


# Основной посредник между выводном в консоль через View и Manager.

class Controller:

    def __init__(self):
        self.controller = Manager()

    # def create_database(self):
    #     self.controller.create_connect_database()

    def create_table(self):
        self.controller.create_table()

    def insert_data(self, *args, **kwargs):
        self.controller.insert_employee(*args, **kwargs)

    def show_data(self):
        self.controller.show_all_employees()

    def logging(self):
        pass

    def execute_large_request(self):
        self.controller.execute_large_request()

    def show_all_employees_for_large_request(self):
        self.controller.show_all_employees_for_large_request_not_optimal()

    def show_all_employees_for_large_request_not_optimal(self):
        self.controller.show_all_employees_for_large_request_optimal()

    def drop_table(self):
        self.controller.drop_table()
