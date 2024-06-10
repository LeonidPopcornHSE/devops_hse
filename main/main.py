from employee import Employee

employee1 = Employee("Андрей", "Инженер", 2000)
employee2 = Employee("Мария", "Менеджер",5000)
employee1.display_employee()
employee2.display_employee()
print("Всего сотрудников: %d" % Employee.emp_count)
employee3 = Employee("Юлия", "Переводчик", 800)
employee1.add_employee_to_project("Разработка")
employee2.add_employee_to_project("Разработка")
employee3.add_employee_to_project("Организация")
Employee.info_projects()
employee2.del_employee_from_project("Разработка")
Employee.info_projects()
