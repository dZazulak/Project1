from custom_exceptions.employee_is_not_logged_in_exception import EmployeeIsNotLoggedInException
from custom_exceptions.employee_email_not_found_exception import EmployeeEmailNotFoundException
from custom_exceptions.invalid_email_exception import InvalidEmailException
from custom_exceptions.invalid_password_exception import InvalidPasswordException
from data_access_layer.implementation_classes.employee_dao_imp import EmployeeDAOImp
from entities.employee import Employee
from service_layer.implementation_services.employee_service_imp import EmployeeServiceImp

employee_dao = EmployeeDAOImp()
employee_service = EmployeeServiceImp(employee_dao)

employee_logged_in: Employee = Employee(1, "Alex", "Lara", "Alex.Lara@shield.inc", "alex")

employee_wrong_password: Employee = Employee(2, "Eric", "Jennings", "Eric.Jennings@shield.inc", "eeric")

employee_with_wrong_email: Employee = Employee(2, "Eric", "Jennings", "Erc.Jennings@shield.inc", "eric")


def test_get_employee_id_fail():
    try:
        employee_service.service_get_employee_by_email(employee_with_wrong_email)
        assert False
    except EmployeeEmailNotFoundException as e:
        assert str(e) == "Employee email was not found."


def test_check_employee_login_email_fail():
    try:
        employee_service.service_check_employee_login("alex.lara@shield.com", "alex")
        assert False
    except InvalidEmailException as e:
        assert str(e) == "Invalid email"


def test_check_employee_login_password_fail():
    try:
        employee_service.service_check_employee_login("alex.lara@shield.inc", "alexx")
        assert False
    except InvalidPasswordException as e:
        assert str(e) == "Invalid password"
