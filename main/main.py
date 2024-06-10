from employee import Employee

employee1 = Employee("Андрей", "Инженер", 2000)
employee2 = Employee("Мария", "Менеджер",5000)
employee1.display_employee()
employee2.display_employee()
print("Всего сотрудников: %d" % Employee.emp_count)