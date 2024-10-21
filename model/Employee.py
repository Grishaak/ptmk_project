import datetime


class Employee:
    def __init__(self, firstname, middlename, lastname, birthdate, sex):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.birthdate = birthdate
        self.sex = sex

    def get_age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year
        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1
        return age

    def get_full_name(self):
        return f"{self.firstname} {self.middlename} {self.lastname}"

    def __str__(self):
        return f"Employee: {self.get_full_name()}, Age: {self.get_age()}, Sex: {self.sex}"

    def get_values(self):
        return self.firstname, self.middlename, self.lastname, self.birthdate, self.sex
