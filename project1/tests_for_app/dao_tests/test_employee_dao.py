from data_access_layer.implementation_classes.employee_dao_imp import EmployeeDAOImp
from entities.employee import Employee

employee_dao = EmployeeDAOImp()
# employee_one: Employee = Employee(1, "Alex", "Lara", "Alex.Lara@shield.inc", "alex")
#
# employee_two: Employee = Employee(2, "Eric", "Jennings", "Eric.Jennings@shield.inc", "eric")


def test_get_employee_by_email():
    returned_employee: Employee = employee_dao.get_employee_by_email("alex.lara@shield.inc")
    assert returned_employee.employee_id == 1


def test_get_all_employees_success():
    employee_list = employee_dao.get_all_employees()
    assert len(employee_list) >= 2


def test_check_employee_login():
    employee = employee_dao.get_employee_by_email("alex.lara@shield.inc")
    employee_login = employee_dao.check_employee_login(employee.email, employee.passcode)
    assert (employee_login.employee_id == 1 and employee_login.passcode == "alex")
