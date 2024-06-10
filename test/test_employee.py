import pytest

from main.employee import Employee
def test_create_employee():
    employee1 = Employee("Иван", "Менеджер", 6000)
    assert employee1.name == "Иван"
    assert employee1.position == "Менеджер"
    assert employee1.salary == 6000

def test_create_employee_fail():
    with pytest.raises(ValueError):
        Employee("Иван", "Менеджер", "6000")

def test_count_employee():
    employee2 = Employee("Андрей", "Инженер", 2000)
    employee3 = Employee("Мария", "Менеджер",5000)
    assert Employee.emp_count == 3
    employee4 = Employee("Юлия", "Переводчик", 800)
    assert Employee.emp_count == 4
