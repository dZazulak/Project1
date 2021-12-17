from abc import ABC, abstractmethod
from entities.employee import Employee


class EmployeeDAO(ABC):

    @abstractmethod
    def get_all_employees(self) -> list[Employee]:
        pass

    @abstractmethod
    def check_employee_login(self, email: str, passcode: str) -> Employee:
        pass

    @abstractmethod
    def get_employee_by_email(self, email: str) -> Employee:
        pass
