class Person:
    def __init__(self, name, surname, age, phone):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone = phone

    def get_person(self):
        return self.__dict__


class Employee(Person):
    def __init__(self, name, surname, age, phone, salary):
        Person.__init__(self, name, surname, age, phone)
        self.salary = salary

    def get_employee(self):
        return self.__dict__

    def pay_tax(self):
        if self.salary > 30000 and self.age < 32:
            return "Paga impuestos"
        else:
            return "No paga impuestos"
