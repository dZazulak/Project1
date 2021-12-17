from abc import ABC, abstractmethod
from entities.employee import Employee
from entities.reimbursement import Reimbursement


class EmployeeService(ABC):

    @abstractmethod
    def service_get_employee_by_email(self, employee_id: int) -> Employee:
        pass

    @abstractmethod
    def service_get_all_employees(self) -> list[Employee]:
        pass

    @abstractmethod
    def service_check_employee_login(self, email: str, passcode: str) -> Employee:
        pass

