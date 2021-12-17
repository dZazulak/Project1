from abc import ABC, abstractmethod
from entities.manager import Manager


class ManagerDAO(ABC):

    @abstractmethod
    def get_manager_by_email(self, email: str) -> Manager:
        pass

    @abstractmethod
    def get_all_managers(self) -> list[Manager]:
        pass

    @abstractmethod
    def check_manager_login(self, email: str, passcode: str):
        pass

