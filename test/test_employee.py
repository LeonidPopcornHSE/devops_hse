import pytest

from main.employee import Employee
def test_create_employee():
    employee = Employee("Иван", "Менеджер", 6000)
    assert employee.name == "Иван"
    assert employee.position == "Менеджер"
    assert employee.salary == 6000

def test_create_employee_fail():
    with pytest.raises(ValueError):
        Employee("Иван", "Менеджер", "6000")

def test_count_employee():
    employee1 = Employee("Андрей", "Инженер", 2000)
    employee2 = Employee("Мария", "Менеджер",5000)
    assert Employee.emp_count == 2
