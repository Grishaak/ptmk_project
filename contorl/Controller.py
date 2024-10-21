from model.Manager import Manager


class Controller:

    def __init__(self):
        self.controller = Manager()

    def create_database(self):
        self.controller.create_connect_database()

    def create_table(self):
        self.controller.create_table()

    def insert_data(self, *args, **kwargs):
        # employee = self.controller.create_employee()
        self.controller.insert_employee(*args, **kwargs)

    def logging(self):
        pass
