from model.Manager import Manager


class Controller:

    def __init__(self):
        self.controller = Manager()

    def create_database(self):
        self.controller.create_connect_database()

    def create_table(self):
        self.controller.create_table()

    def insert_data(self, *args, **kwargs):
        self.controller.insert_employee(*args, **kwargs)

    def show_data(self):
        self.controller.show_all_employees()

    def logging(self):
        pass

    def close_connection(self):
        self.controller.close_connection()
