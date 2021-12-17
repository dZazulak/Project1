from custom_exceptions.employee_email_not_found_exception import EmployeeEmailNotFoundException
from custom_exceptions.invalid_email_exception import InvalidEmailException
from custom_exceptions.invalid_password_exception import InvalidPasswordException
from data_access_layer.implementation_classes.employee_dao_imp import EmployeeDAO
from entities.employee import Employee
from service_layer.abstract_services.employee_service import EmployeeService


class EmployeeServiceImp(EmployeeService):
    def __init__(self, employee_dao: EmployeeDAO):
        self.employee_dao = employee_dao

    def service_get_employee_by_email(self, email: str) -> Employee:
        employee_list = self.employee_dao.get_all_employees()
        for existing_employee in employee_list:
            if existing_employee.email == email:
                return self.employee_dao.get_employee_by_email(email)
        raise EmployeeEmailNotFoundException("Employee email was not found.")

    def service_check_employee_login(self, email: str, passcode: str) -> Employee:
        employee_list = self.employee_dao.get_all_employees()
        for current_employee in employee_list:
            if current_employee.email == email:
                if current_employee.passcode == passcode:
                    return self.employee_dao.check_employee_login(email, passcode)
                raise InvalidPasswordException("Invalid password")
        raise InvalidEmailException("Invalid email")

    def service_get_all_employees(self) -> list[Employee]:
        return self.employee_dao.get_all_employees()
