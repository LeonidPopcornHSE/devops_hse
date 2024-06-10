class Employee:
    emp_count = 0
    projects = {}
    # add projects in office

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

    def add_employee_to_project(self, name_project):
        if name_project not in Employee.projects:
            Employee.projects[name_project] = set([self.name])
        else:
            Employee.projects[name_project].add(self.name)

    def del_employee_from_project(self, name_project):
        if name_project not in Employee.projects:
            raise Exception
        else:
            Employee.projects[name_project].discard(self.name)

    @classmethod
    def info_projects(cls):
        print(f'Количество проектов: {len(Employee.projects)}')
        print("Информация о каждом из проектов:")
        i = 1
        for key in Employee.projects.keys():
            print(f"    {i}. Название: {key}")
            for participant in Employee.projects[key]:
                print("         ", participant)
            i += 1
