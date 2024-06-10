class Employee:
    emp_count = 0

    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        if isinstance(salary, int) or isinstance(salary, float):
            self.salary = salary
        else:
            raise ValueError
        Employee.emp_count += 1

    def display_count(self):
        print('Всего сотрудников: %d' % Employee.empCount)

    def display_employee(self):
        print('Имя: {}. Зарплата: {}'.format(self.name, self.salary))